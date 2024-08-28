#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: fabienfrfr
TESTS FILE
"""

from pixelbytes import *
from datasets import load_dataset



### basic test
if __name__ == '__main__' :
    # train part
    hf_dataset = load_dataset("ffurfaro/PixelBytes-Pokemon")
    tokenizer = PixelBytesTokenizer()
    generator = SequenceGenerator(tokenizer)
    # initialize sequence (ARRAY)
    first_sequence = np.array(hf_dataset["train"]['pixelbyte'][0])
    for start in np.arange(0,1000,50) :
        start_lenght, sup_lenght = 64, 50
        # init
        reference_sequence = first_sequence[start: start + start_lenght + sup_lenght]
        start_sequence = reference_sequence[:start_lenght]
        end_sequence = reference_sequence[start_lenght : start_lenght + sup_lenght]
        # reset
        generator.reset(start_sequence)
        generated_sequence = generator.update_sequence(end_sequence[:,1,1])
        print(np.mean(reference_sequence - generated_sequence)) ## all zero with 50 lenght ! prefer 64 to be large
    '''
    tokenizer = PixelBytesTokenizer()
    model = SimpleRNNModel.from_pretrained("ffurfaro/PixelBytes-Pokemon", subfolder="rnn_bi_pxby_81_dim_64_state_2_layer_last")
    #model = bMamba.from_pretrained("ffurfaro/PixelBytes-Pokemon", subfolder="rnn_bi_pxby_81_dim_64_state_2_layer_last")
    # generate and display
    generator = SequenceGenerator(tokenizer)
    reconstructor = SequenceReconstructor(tokenizer)
    # generate complete sequence

    complete_sequence = generator.generate_complete(start_sequence, max_length=0, temperature=0.7) 
    # reconstruction 2D complexe ! car si on commence au milieu de l'image, il est compliqué de savoir les bords !
    print(complete_sequence)
    # Génération en streaming
    print("\nGénération en streaming (incluant la séquence initiale):")
    #for matrix in generator.generate_stream(start_sequence, max_length=25, temperature=0.7):
    #    print(matrix)
    # display generated sequence
    """
    # generate complete sequence
    first_sequence = np.array(hf_dataset["train"]['pixelbyte'][0])[:,1,1]
    #start_sequence = [tokenizer.vocab[t] for t in [b't',b't',b'\n',b't',b'\n',(0,0,0),(252,252,252),(252,252,252),b'\t',(252,252,252),(252,252,252),(0,0,0),b'\n',b't',b't']]
    start_sequence = first_sequence[:150].tolist() # image not work ?
    complete_sequence = generator.generate_complete(start_sequence, max_length=300, temperature=0.7)
    print(complete_sequence)
    # Génération en streaming
    print("\nGénération en streaming (incluant la séquence initiale):")
    """
    """
    # Génération complète
    reconstructor = SequenceReconstructor(tokenizer)
    for token_id in complete_sequence[:,1,1]:
        reconstructor.process(token_id)
    result = reconstructor.get_result()
    display_result(result)
    """
    """
    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    
    for inputs, targets in tqdm(train_loader, desc="Training"):
        outputs = model(inputs)
        print(inputs[:,-1,1,1], outputs.max(1)[1])
        break
    
    """
    """
    ds = hf_dataset["train"].train_test_split(test_size=0.1)
    train_dataset = PxByDataset(ds["train"]["pixelbyte"], seq_length=256, stride=128)
    test_dataset = PxByDataset(ds["test"]["pixelbyte"], seq_length=256, stride=128)

    # tokenizer config
    tokenizer = PixelBytesTokenizer()
    #tokenizer.save_vocabulary("./models")   # Sauvegarder le vocabulaire
    #push_tokenizer_to_hub(tokenizer)
    
    #tokenizer = PixelBytesTokenizer.from_pretrained("ffurfaro/PixelBytes-Pokemon")
    # train model & config
    vocab_size = tokenizer.__len__()
    model_config = ModelConfig(dim=81, d_state=64, depth=2, vocab_size=vocab_size, bidirectional=False)
    # train simple model (one epoch)
    model = SimpleRNNModel(model_config) #SimpleTransformerModel(config)
    

    token = None #input("Input Hugging Face Token: ")
    train_config = TrainConfig(model=model, model_config=model_config, dataset_name="PixelBytes-Pokemon", hf_token=token,
                               train_dataset=train_dataset,test_dataset=test_dataset, num_epochs=2, repo_name="PixelBytes-Pokemon")
    trainer = Trainer(train_config)
    trainer.train_and_evaluate()
    """
    """
    ## Construct Pokemon datasets
    # get miniatures
    miniatures = get_pkmns_miniatures()
    # construct dataset
    dataset = create_pkmn_dataset(miniatures)
    # push to hub
    #push_dataset(dataset, 'ffurfaro/PixelBytes-Pokemon')
    # show
    img = dataset['image'][0] # Image.open(io.BytesIO(dataset['image'][0]))
    plt.imshow(np.array(img)); plt.show()
    """
    """
    dataset = load_dataset("ffurfaro/PixelBytes-Pokemon")
    dataset = dataset.remove_columns('name')
    dataset = add_pixelbyte_columns(dataset)
    # push to hub
    push_dataset(dataset, 'ffurfaro/PixelBytes-Pokemon')
    """
    
    """
    dataset = load_dataset("ffurfaro/PixelBytes-Pokemon")
    pixelbytes = [np.array(pb) for pb in dataset['train']['pixelbyte']]
    tokenizer = PixelBytesTokenizer()

    p = pixelbytes[0]
    tokens = tokenizer.convert_ids_to_tokens(p[:,1,1])
    img = reconstruct_imgs(tokens[:np.random.randint(50,len(tokens)//2)])[0]["image"]
    plt.imshow(img);plt.show()
    """
    
    
    
    
    
    
    '''
    
    
    
    
    
    
    
    
    
    
