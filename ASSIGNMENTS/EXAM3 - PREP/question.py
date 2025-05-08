# directory JSON:
{
    "\\main": {
        "\\photos": {
            "\\Summer Trip": {
                "beach.png" : 2400,
                "mountain.png" : 1200,
                "lasagna.png" : 2000
            },
            "\\Winter Trip": {
                "cabin.png" : 2000,
                "skiing.png" : 1800
            }
        },
        "\\Homework": {
            "\\Math": {
                "Algebra.pdf" : 1000,
                "Statistics.txt" : 1300,
                "\\Physics" : {
                    "Mechanics.pdf" : 2000,
                    "Electromagnetism.txt" : 2200
                }
            }
        }
    },
    "\\backup": {
        "\\photos" : {
            "\\Summer Trip": {
                "beach.png" : 2400,
                "mountain.png" : 1200,
                "city.mp4" : 5800,
                "forest.mp4" : 5600,
                "lasagna.png" : 2000
            }
        }
    }
}

# Write a recursive function to find the total size of the directory, as well as the number of each type of files in it.
# The program should export the results to a JSON file with the following structure:
# {
#     "total_size": <total_size>,
#     "file_count": {
#         "txt": <number_of_txt_files>,
#         "png": <number_of_png_files>,
#         "pdf": <number_of_pdf_files>,
#         ...
#     }
# }
# Lastly, the program should print the contents of the exported JSON file to the console.
# The program should take any arbitrary JSON representation of a directory with the sizes as input.