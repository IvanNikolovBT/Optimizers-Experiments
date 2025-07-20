def process_text_file(file_path):
    try:
        
        with open(file_path, 'r') as file:
            lines = file.readlines()
        cross,test,rmse=0,0,0
        for line in lines[1:]:
            words = line.strip().split(' ') 
            
            
            cross+=float(words[2])
            test+=float(words[3])
            rmse+=float(words[4])

        print(f'Cross {round(cross/9,4)}')
        print(f'Test {round(test/9,4)}')
        print(f'Rmse {round(rmse/9,4)}')
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


process_text_file("/home/ivan/Desktop/BIP_lokalno/final_data.txt")