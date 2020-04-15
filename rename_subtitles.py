import os, glob

main_path = os.path.join('/mnt', 'c', 'Users', 'Gustavo', 'Videos')
os.chdir(os.path.join(main_path))

for root, directories, files in os.walk(main_path):
    mkv = glob.glob(os.path.join(root, '*mkv'))
    mp4 = glob.glob(os.path.join(root, '*mp4'))
    srt = glob.glob(os.path.join(root, '*srt'))

    movies = mkv + mp4
    if len(movies):
        if len(movies) == 1 and len(srt) == 1:
            d = root.split('/')[-1]
            # print(f'{d}\tMovies: {len(movies)} Srt: {len(srt)}')
            movie_name, movie_ext = os.path.splitext(movies[0].split('/')[-1])
            sub_name, sub_ext = os.path.splitext(srt[0].split('/')[-1])
            # print(movie_name)
            # print(sub_name)
            # if sub_name != movie_name:
                # print(f'Renaming subtitles for {movie_name}\n')
                # os.chdir(root)
                # os.rename(srt[0], f'{movie_name}.srt')


for root, dirs, _ in os.walk(main_path):
    print(dirs)

# for *dirs, _ in os.walk(main_path):
#     for d in dirs:
#         if len(d):
#             print(d)