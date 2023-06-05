from interface.graph_encoder_painter import GraphEncoderPainter

def start():
    encode_options = ['encode', 'e']
    decode_options = ['decode', 'd']

    print('Hello! Please pick whether you want to encode (E) or \
          decode (D) the graph using the Pruefer code. Press q to quit.')

    user_input = input().lower()

    if user_input in encode_options:
        GraphEncoderPainter().perform()
    elif user_input in decode_options:
        # GraphDecoder.perform()
        pass
    elif user_input == 'q':
        print('Goodbye')
        return
    else:
        print('Please enter correct option')
        start()

start()