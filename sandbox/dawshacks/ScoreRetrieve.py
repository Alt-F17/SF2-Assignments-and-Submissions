import shutil
import zipfile
import re
import statistics
from pathlib import Path
import json

def main():
    downloads = Path(r"C:\Users\felix\Onedrive - Dawson College\Downloads")
    cwd = Path.cwd()
    scores = {}

    for zip_path in downloads.glob("Grading Rubric - *.zip"):
        grader = zip_path.stem.split("Grading Rubric - ", 1)[1]
        local_zip = cwd / zip_path.name
        shutil.copy(zip_path, local_zip)

        extract_dir = cwd / zip_path.stem
        extract_dir.mkdir(exist_ok=True)
        with zipfile.ZipFile(local_zip, "r") as z:
            z.extractall(extract_dir)

        for html_file in extract_dir.rglob("*.html"):
            content = html_file.read_text(encoding="utf-8")
            tm = re.search(r"TEAM:\s*([^<\r\n]+)", content)
            gm = re.search(r"Final Score:\s*([\d.]+)%", content)
            if not (tm and gm):
                continue
            team = tm.group(1).strip()
            grade = float(gm.group(1))
            print(f"Team {team}, graded by {grader}: {grade}%")
            if grade > 0:
                scores.setdefault(team, []).append(grade)

        shutil.rmtree(extract_dir)
        local_zip.unlink()

    for team, vals in scores.items():
        if vals:
            avg = statistics.mean(vals)
            print(f"Team {team} AVG score: {avg:.2f}%")

    print(">>> Leaderboard:")
    sorted_teams = sorted(scores.items(),
                          key=lambda kv: statistics.mean(kv[1]) if kv[1] else 0,
                          reverse=True)
    
    for team, vals in sorted_teams:
        if vals:
            avg = statistics.mean(vals)
            print(f"Team {team}: {avg:.2f}%")
    
    json_data = {}
    for team, vals in sorted_teams:
        if vals:
            avg = statistics.mean(vals)
            json_data[team] = {"average": avg}
    
    with open(cwd / r"C:\Users\felix\OneDrive - Dawson College\Class Files\SF2 - Coding\SF2-Assignments-and-Submissions\sandbox\dawshacks\leaderboard.html", "w", encoding='utf-8') as file:
        team_population = ""
        for team, vals in sorted_teams:
            if vals:
                average = statistics.mean(vals)
                team_population += f'            "{team}": {{"average": {average/100}}},\n'
                print(team_population)
        with open(cwd / "leaderboard.json", "w") as json_file:
            json.dump(json_data, json_file)
        file.write(
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DawsHacks Leaderboard</title>
    <style>
        :root {
            --accent: #659cde;
            --accent-dark: #4a7ab8;
            --bg-color: #f8f9fa;
            --fg: #333;
            --gold: #fcf1b2;
            --silver: #d9d9d9;
            --bronze: #cfa983;
            --honorable: #e6f2ff;
        }

        body {
            background-color: var(--bg-color);
            color: var(--fg);
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }

        header {
            text-align: center;
            padding: 20px;
            background-color: var(--accent);
            color: white;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        header img {
            max-width: 100px;
            height: auto;
        }

        header h1 {
            margin: 10px 0;
        }

        .code {
            font-family: monospace;
            color: #ffffff;
            font-size: 35px;
        }

        main {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 20px;
        }

        #loading {
            text-align: center;
            font-size: 1.2em;
            margin: 20px;
        }

        #leaderboard {
            width: 100%;
            max-width: 800px;
            border-collapse: collapse;
        }

        #leaderboard th, #leaderboard td {
            padding: 10px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }

        #leaderboard th {
            background-color: var(--accent-dark);
            color: white;
        }

        #leaderboard tbody tr:nth-child(even) {
            background-color: #fefefe;
        }

        #leaderboard tbody tr:nth-child(odd) {
            background-color: white;
        }

        #leaderboard tbody tr.rank-1 {
            background-color: var(--gold);
            font-weight: bold;
        }

        #leaderboard tbody tr.rank-2 {
            background-color: var(--silver);
            font-weight: bold;
        }

        #leaderboard tbody tr.rank-3 {
            background-color: var(--bronze);
            font-weight: bold;
        }

        #leaderboard tbody tr.rank-4, #leaderboard tbody tr.rank-5 {
            background-color: var(--honorable);
        }

        #leaderboard tbody tr {
            transition: background-color 0.3s;
        }

        #leaderboard tbody tr.rank-other:hover {
            background-color: #e0e0e0;
        }

        .fade-in {
            animation: fadeIn 0.5s ease-in both;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        .team-icon {
            width: 20px;
            height: 20px;
            vertical-align: middle;
            margin-right: 5px;
        }

        .honorable-mention {
            font-style: italic;
            font-size: 0.9em;
            color: #666;
        }

        @media (max-width: 600px) {
            #leaderboard {
                display: block;
                overflow-x: auto;
            }

            #leaderboard th, #leaderboard td {
                padding: 5px;
                font-size: 0.9em;
            }
        }
        thead, tr {
            border-radius: 2.5vmin;
        }
        thead {
            border-top: 8px solid var(--accent-dark);
        }
        tr {
            border-radius: 1.25vmin;
            /* border: 10px solid red; */
            border-right: 10px solid var(--accent-dark);
            border-left: 10px solid var(--accent-dark);
            overflow: hidden;
        }
        tr:last-of-type {
            border-bottom: 10px solid var(--accent-dark);
        }
    </style>
</head>
<body>
    <header>
        <img src="DawsHacks Crow Logo.png" alt="DawsHacks Logo">
        <h1><span class="code">&lt;miniDawsHacks.25&gt;</span> Leaderboard</h1>
    </header>
    <main>
        <div id="loading">Loading...</div>
        <table id="leaderboard">
            <thead>
                <tr>
                    <th>Rank</th>
                    <th>Team</th>
                    <th>Score (%)</th>
                </tr>
            </thead>
            <tbody>
                <!-- Table rows will be inserted here -->
            </tbody>
        </table>
    </main>
    <script>
        const fallbackData = {
"""
+ team_population[:-1] +
"""
        };

        const terminalIconSVG = '<svg class="team-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M21 3H3c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h18c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H3V5h18v14zM5 7h14v2H5V7zm0 4h14v2H5v-2zm0 4h14v2H5v-2z"/></svg>';

        let usingFallback = false;

        // Try multiple possible paths to the JSON file
        fetch('./leaderboard.json')
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Network response was not ok: ${response.status} ${response.statusText}`);
                }
                return response.json();
            })
            .then(data => {
                if (!data || Object.keys(data).length === 0) {
                    throw new Error('JSON data is empty or invalid');
                }
                console.log('Successfully loaded data:', data);
                processData(data);
            })
            .catch(error => {
                console.error('Error loading leaderboard data:', error);
                
                // Try an alternative path as fallback
                fetch('/leaderboard.json')
                    .then(response => response.ok ? response.json() : Promise.reject('Alternative path failed'))
                    .then(data => {
                        console.log('Loaded from alternative path');
                        processData(data);
                    })
                    .catch(err => {
                        console.error('All fetch attempts failed:', err);
                        usingFallback = true;
                        processData(fallbackData);
                    });
            });

        function processData(data) {
            const teams = Object.entries(data).map(([teamName, teamData]) => [teamName, teamData.average]);
            teams.sort((a, b) => b[1] - a[1]);

            const tbody = document.querySelector('#leaderboard tbody');
            tbody.innerHTML = ''; // Clear any existing rows

            teams.forEach((team, index) => {
                const rank = index + 1;
                const teamName = team[0];
                const score = team[1];

                const tr = document.createElement('tr');
                tr.classList.add('fade-in');
                tr.style.animationDelay = `${index * 0.1}s`;

                if (rank === 1) {
                    tr.classList.add('rank-1');
                } else if (rank === 2) {
                    tr.classList.add('rank-2');
                } else if (rank === 3) {
                    tr.classList.add('rank-3');
                } else if (rank === 4 || rank === 5) {
                    tr.classList.add('rank-4');
                } else {
                    tr.classList.add('rank-other');
                }

                const rankCell = document.createElement('td');
                let rankDisplay = rank;
                if (rank === 1) {
                    rankDisplay = '🥇';
                } else if (rank === 2) {
                    rankDisplay = '🥈';
                } else if (rank === 3) {
                    rankDisplay = '🥉';
                }
                rankCell.textContent = rankDisplay;
                tr.appendChild(rankCell);

                const teamCell = document.createElement('td');
                let teamDisplay = `${terminalIconSVG} ${teamName}`;
                if (rank === 4 || rank === 5) {
                    teamDisplay += ' <span class="honorable-mention">(Honorable mention)</span>';
                }
                teamCell.innerHTML = teamDisplay;
                tr.appendChild(teamCell);

                const scoreCell = document.createElement('td');
                scoreCell.textContent = `${(score * 100).toFixed(2)}%`;
                tr.appendChild(scoreCell);

                tbody.appendChild(tr);
            });

            document.getElementById('loading').style.display = 'none';
            if (usingFallback) {
                document.getElementById('fallback-message').style.display = 'block';
            }
        }
    </script>
</body>
</html>
"""
)
   
    print(f"\n>>> Above team scores have been saved to {Path.cwd() / 'leaderboard.txt'}")

if __name__ == "__main__":
    main()