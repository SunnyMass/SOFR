import os

def test_one_model():
    output_json_path = f"TCSVT2024_psnr_sofr.json"
    image_model_path = './checkpoints/cvpr2023_image_psnr.pth.tar'
    command_line = (" python test_video_hierarchical.py"
                    f" --i_frame_model_path  {image_model_path}"
                    f" --p_frame_model_path ./checkpoints/psnr_model.pth.tar"
                    " --rate_num 4"
                    " --calc_ssim 0"
                    " --test_config recommended_test_full_results_IP32.json --cuda 1 -w 8"
                    f" --output_path {output_json_path} --save_decoded_frame 1 --decoded_frame_path ./decoded_frames"
                    f" --write_stream 1 --stream_path ./bin")

    print(command_line)
    os.system(command_line)

def main():
    test_one_model()


if __name__ == "__main__":
    main()
