import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


REGION_ACCOUNT_MAP = {
    "us-east-1": "865070037744",
    "us-east-2": "057799348421",
    "us-west-2": "594846645681",
    "eu-west-1": "985815980388",
    "eu-central-1": "446921602837",
    "ap-northeast-1": "977537786026",
    "ap-northeast-2": "745090734665",
    "ap-southeast-2": "666831318237",
    "ap-southeast-1": "192199979996",
    "ap-south-1": "077584701553",
    "ca-central-1": "470592106596",
    "eu-west-2": "856760150666",
    "us-west-1": "382657785993",
    "eu-west-3": "843114510376",
    "eu-north-1": "136758871317",
    "sa-east-1": "270155090741",
    "ap-east-1": "822005858737",
}

MODEL_PACKAGE_ARN = (
    "arn:aws:sagemaker:%s:%s:model-package/vitechlab-ppe-model-v3-1-290ec9dbb1ff9b555c3e5e6831fe4769"
)

colors = [
    # Bare Head
    [0.716, 0.170, 0.427],

    # Helmet
    [0.388, 0.631, 0.111],

    # Welding Mask
    [0.098, 0.680, 0.468],

    # Ear Protection
    [0.163, 0.075, 0.997],

    # NO Visibility Vest
    [0.849, 0.471, 0.491],

    # High Visibility Vest
    [0.595, 0.554, 0.006],

    # Person
    [0.699, 0.193, 0.917]
]

classes = ['Bare Head', 'Helmet', 'Welding Mask', 'Ear Protection',
           'NO Visibility Vest', 'High Visibility Vest', 'Person']


def get_model_package_arn(region):
    account = REGION_ACCOUNT_MAP[region]
    
    return MODEL_PACKAGE_ARN % (region, account)


def visualize_detection(img_file, dets, save_path=None):
        img=mpimg.imread(img_file)
        plt.imshow(img)
        height = img.shape[0]
        width = img.shape[1]
        
        for det in dets:
            x0, y0, x1, y1, score, _, klass = det
            
            cls_id = int(klass)
            xmin = x0
            ymin = y0
            xmax = x1
            ymax = y1
            rect = plt.Rectangle((xmin, ymin), xmax - xmin,
                                 ymax - ymin, fill=False,
                                 edgecolor=colors[cls_id],
                                 linewidth=3.5)
            plt.gca().add_patch(rect)
            class_name = str(cls_id)
            if classes and len(classes) > cls_id:
                class_name = classes[cls_id]
            plt.gca().text(xmin, ymin - 2,
                            '{:s} {:.3f}'.format(class_name, score),
                            bbox=dict(facecolor=colors[cls_id], alpha=0.3),
                                    fontsize=12, color='white')
        plt.axis('off')
        
        if save_path is not None:
            plt.savefig(save_path, bbox_inches='tight')
        
        plt.show()
