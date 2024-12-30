import re

class a2:
    CATEGORY = "0x_erthor_node👾👾👾/a000_example"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "输入文本": ("STRING", {
                    "default": "1girl, solo, green_eyes, green_hair, white_shirt, white_footwear",
                    "multiline": True
                }),
            }
        }

    OUTPUT_NODE = True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("过滤后的颜色词",)

    FUNCTION = "process_text"

    def process_text(self, 输入文本):
        # 1. 清理输入文本
        clean_text = 输入文本.replace("\n", " ").replace(";", ",")

        # 2. 颜色关键词列表
        color_keywords = r'(white|black|red|green|blue|yellow|pink|purple|orange|brown|gray)'

        # 3. 正则匹配带有颜色和特定部位的关键词
        pattern = rf'\b{color_keywords}_(eyes|hair|shirt|pants|footwear|skirt|coat|jacket|dress|shorts)\b'

        # 4. 查找所有符合条件的颜色提示词
        matches = re.findall(pattern, clean_text)

        # 5. 组合成完整的颜色+部位形式，并去重、排序
        filtered_keywords = sorted(set(["_".join(match) for match in matches]))

        # 6. 返回逗号分隔的字符串
        return (", ".join(filtered_keywords),)