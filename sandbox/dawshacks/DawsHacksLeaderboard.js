const express = require('express');
const fs = require('fs');
const path = require('path');
const unzipper = require('unzipper');
const cheerio = require('cheerio');

const app = express();
const DOWNLOADS = path.join(require('os').homedir(), 'Downloads');
const WORKDIR = __dirname;

async function scanScores() {
  const scores = {};
  const files = await fs.promises.readdir(DOWNLOADS);
  for (let fn of files.filter(f => f.startsWith('Grading Rubric - ') && f.endsWith('.zip'))) {
    const grader = fn.replace('Grading Rubric - ', '').replace('.zip','');
    const zipPath = path.join(DOWNLOADS, fn);
    const extractDir = path.join(WORKDIR, fn.replace('.zip',''));
    await fs.promises.mkdir(extractDir, { recursive:true });
    await fs.createReadStream(zipPath)
      .pipe(unzipper.Extract({ path: extractDir }))
      .promise();
    for (let htmlFile of await fs.promises.readdir(extractDir)) {
      if (!htmlFile.endsWith('.html')) continue;
      const $ = cheerio.load(await fs.promises.readFile(path.join(extractDir,htmlFile)));
      const team = $('.s0').first().text().trim() || $('td:contains("Final Score")').parent().find('td').last().text();
      const match = $.html().match(/Final Score:\s*([\d.]+)%/);
      if (team && match) {
        scores[team] = scores[team]||[];
        scores[team].push(parseFloat(match[1]));
      }
    }
    // cleanup
    fs.rmSync(extractDir, { recursive:true, force:true });
  }
  // compute averages
  return Object.entries(scores).map(([team, arr])=>{
    const avg = arr.reduce((a,b)=>a+b,0)/arr.length;
    return { team, scores: arr, avg };
  }).sort((a,b)=>b.avg - a.avg);
}

app.use(express.static(WORKDIR));

app.get('/api/leaderboard', async (_, res) => {
  res.json(await scanScores());
});

app.listen(3000, ()=>console.log('Leaderboard at http://localhost:3000/DawsHacksLeaderboard.html'));