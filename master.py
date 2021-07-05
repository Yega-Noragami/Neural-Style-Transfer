import cv2
import os 

class NeuralStyleTransfer:
    
    '''
    This class is a representation of Neural Style Transfer application on images
    video implementation is coming soon!
    '''

    #Image Variable
    base ='./Images/base.png' 
    style= './Images/style.png'



    #initialisation
    def __init__(self , base , style):
        self.b =base
        self.s = style

    # Model Train cmd line implemetation 
    @staticmethod
    def model_train():
        ''' 
        TO RUN: 
        python {dir_path}/{NETWORK} {CONTENT_IMAGE_FN} {STYLE_IMAGE_FN} {RESULT_PREFIX} \
  --image_size {IMAGE_SIZE} --content_weight {CONTENT_WEIGHT} --style_weight \
  {STYLE_WEIGHT} --style_scale {STYLE_SCALE} --total_variation_weight \
  {TOTAL_VARIATION_WEIGHT} --content_loss_type {CONTENT_LOSS_TYPE} --num_iter \
  {NUM_ITERATIONS} --model {MODEL} --rescale_image {RESCALE_IMAGE} \
  --maintain_aspect_ratio {MAINTAIN_ASPECT_RATIO} --content_layer {CONTENT_LAYER} \
  --init_image {INITIALIZATION_IMAGE} --pool_type {POOLING_TYPE} --preserve_color \
  {PRESERVE_COLOR} --min_improvement {MIN_IMPROVEMENT}
        '''

        cmd = 'python {dir_path}/{NETWORK} {CONTENT_IMAGE_FN} {STYLE_IMAGE_FN} {RESULT_PREFIX} \
  --image_size {IMAGE_SIZE} --content_weight {CONTENT_WEIGHT} --style_weight \
  {STYLE_WEIGHT} --style_scale {STYLE_SCALE} --total_variation_weight \
  {TOTAL_VARIATION_WEIGHT} --content_loss_type {CONTENT_LOSS_TYPE} --num_iter \
  {NUM_ITERATIONS} --model {MODEL} --rescale_image {RESCALE_IMAGE} \
  --maintain_aspect_ratio {MAINTAIN_ASPECT_RATIO} --content_layer {CONTENT_LAYER} \
  --init_image {INITIALIZATION_IMAGE} --pool_type {POOLING_TYPE} --preserve_color \
  {PRESERVE_COLOR} --min_improvement {MIN_IMPROVEMENT}'
        
        os.system(cmd)


    def setup(self):
        dir_path = "Neural-Style-Transfer"

        '''
        Note There are 2 network types
        1. Network : for original style transfer images
        2. INetwork : improvrd style transfer (default)
        '''

        '''Hyperparamete selection '''

        # Image size
        IMAGE_SIZE = 500

        # Loss Weights
        CONTENT_WEIGHT = 0.025
        STYLE_WEIGHT = 1.0
        STYLE_SCALE = 1.0
        TOTAL_VARIATION_WEIGHT = 8.5e-5
        CONTENT_LOSS_TYPE = 0

        # Training arguments
        NUM_ITERATIONS = 10
        MODEL = 'vgg19'
        RESCALE_IMAGE = 'false'
        MAINTAIN_ASPECT_RATIO = 'false'  # Set to false if OOM occurs

        # Transfer Arguments
        CONTENT_LAYER = 'conv' + '5_2'  # only change the number 5_2 to something in a similar format
        INITIALIZATION_IMAGE = 'content'
        POOLING_TYPE = 'max'

        # Extra arguments
        PRESERVE_COLOR = 'false'
        MIN_IMPROVEMENT = 0.0
        '''--------------------------'''

        RESULT_DIR = "Images/"
        RESULT_PREFIX = RESULT_DIR + "gen"
        FINAL_IMAGE_PATH = RESULT_PREFIX + "_at_iteration_%d.png" % (NUM_ITERATIONS)

        self.model_train()
        


    #load images 
    def image_loader(base_img , style_img):
        global base 
        global style 

        base = base_img
        style = style_img


if __name__ == "__main__":
    while True: 
        print('Welcome to Neural Style Transfer')
        print('1. Apply Neural Style Transfer')
        print('6. Exit')

        choice = input("enter your choice: ")
        if choice == '6':
            print('Exiting !')
            break
        else:
            print('your choice is :', choice)

            if choice =='1':
                NeuralStyleTransfer.setup()

            


