def make_album(artista, album, faixas=''):
  x = {'Artista':artista, 'Album':album}
  if faixas:
    x['Faixas'] = faixas
  return x

while True:

  artista = input("Digite o artista ou 'q' para sair: ")
  if artista == 'q':
    break
  albumtitulo = input("Digite o album: ")

  album = make_album(artista.title(),albumtitulo.title())

  print(album)
