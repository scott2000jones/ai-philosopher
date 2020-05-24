from textgenrnn import textgenrnn

textgen = textgenrnn('../weights/tao.hdf5')
textgen.train_from_file('../data/tao-te-ching.txt', num_epochs=1)
textgen.save('../weights/tao.hdf5')
