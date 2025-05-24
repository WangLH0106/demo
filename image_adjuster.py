from PIL import Image, ImageEnhance

def adjust_image(image_path: str, output_path: str, brightness: float = 1.0, contrast: float = 1.0, saturation: float = 1.0):
    """
    调整图片的亮度、对比度和饱和度，并将结果保存到新文件。

    参数:
        image_path (str): 输入图片的路径。
        output_path (str): 处理后图片的保存路径。
        brightness (float): 亮度调整因子。1.0 代表原始亮度。
                            大于1.0会增加亮度，小于1.0会降低亮度。
        contrast (float): 对比度调整因子。1.0 代表原始对比度。
        saturation (float): 饱和度调整因子。1.0 代表原始饱和度。
                              0.0 会使图片变为灰度图。
    """
    try:
        # 1. 打开由 image_path 指定的图像文件。
        img = Image.open(image_path)

        # 2. 应用亮度调整
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(brightness)

        # 3. 在亮度调整后的图像基础上应用对比度调整
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(contrast)

        # 4. 在对比度调整后的图像基础上应用饱和度调整
        enhancer = ImageEnhance.Color(img)
        img = enhancer.enhance(saturation)

        # 5. 将最终处理过的图像保存到 output_path。
        img.save(output_path)
        return True
    except FileNotFoundError:
        print(f"错误：输入图像文件未找到: {image_path}")
        return False
    except Exception as e:
        print(f"处理图像时发生错误: {e}")
        return False

if __name__ == "__main__":
    sample_input_path = "input.jpg"  # 用户需要替换为实际的图片路径
    sample_output_path = "output_adjusted.jpg"
    
    brightness_factor = 1.5
    contrast_factor = 1.2
    saturation_factor = 1.3
    
    print(f"尝试调整图片: {sample_input_path}")
    print(f"亮度因子: {brightness_factor}, 对比度因子: {contrast_factor}, 饱和度因子: {saturation_factor}")
    print(f"请注意：这是一个示例用法。您需要将 '{sample_input_path}' 替换为您自己的有效图片路径才能使其工作。")
    
    success = adjust_image(sample_input_path, sample_output_path, brightness_factor, contrast_factor, saturation_factor)
    
    if success:
        print(f"图片已成功调整并保存到: {sample_output_path}")
    else:
        print(f"图片调整失败。请检查输入文件路径和文件是否有效。")
