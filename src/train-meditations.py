from textgenrnn import textgenrnn

textgen = textgenrnn('../weights/meditations.hdf5')
#textgen = textgenrnn('textgenrnn_weights.hdf5')
textgen.train_from_file('../data/meditations.txt', num_epochs=50)
textgen.save('../weights/meditations.hdf5')
