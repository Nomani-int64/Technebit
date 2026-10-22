Technebit-generators: where the voicebanks come about
======
*锝比特-生成器：声库出料口*

*by Nomani (alias/别名: Nomani_int64 / Nomani-int64)*

## General / 概况

Currently there are three voicebanks embedded in these massive Python modules, which you can simply tell by their file name.

目前这些巨大的 Python 程序编码了三个声库，从文件名就可以看出来。

|                 Voicebank / 声库 | Japanese / 日语                     | Chinese / 汉语          | English / 英语             |
| -------------------------------: | :---------------------------------- | :---------------------- | :------------------------- |
|               File name / 文件名 | `ja_cv.py`                          | `zh_cvv.py`             | `en_c+v.py`                |
|            Completeness / 完成度 | **Complete / 完成**                 | **Complete / 完成**     | Basic functions / 基本功能 |
|           Phonemizing / 音素方案 | CV                                  | CVV (October CV + VV)   | C + V                      |
|                  Aliasing / 标注 | Hiragana + Romaji / 平假名 + 罗马字 | Pinyin / 拼音           | ARPAbet                    |
|     OpenUTaU phonemizer / 音素器 | DEFAULT / 默认                      | ZH CVV (十月式整音扩张) | EN C+V                     |
|    Generating runtime / 生成时长 | ~ 300 s                             | ~ 550 s                 | ~ 60 s                     |
| Result file count / 结果文件数量 | 425 (210 `.wav`s)                   | 879 (437 `.wav`s)       | 113 (54 `.wav`s)           |

## Usage / 使用方法

### Preparation / 准备

The programs should be run on Python 3.12 or above, and require the following modules. You can install them via `pip`.

程序应该在 Python 3.12 或更新版上运行，需要如下模块，可以用 `pip` 安装。

|  Module / 模块 | Usage / 作用                                                                                    |
| -------------: | :---------------------------------------------------------------------------------------------- |
|        `numpy` | Fast and convenient number list operations. / 快速便捷的数列操作。                              |
|   `pedalboard` | Sound filtering. / 声音滤波。                                                                   |
|    `soundfile` | Sound file operation. / 声音文件操作。                                                          |
|  `sounddevice` | Playing sound for preview. / 播放预览音频。                                                     |
| `PIL` (Pillow) | Image processing. / 图像处理。                                                                  |
|      `librosa` | Advanced audio processing, mainly for freq table generating. / 高级音频处理，主要是频率表生成。 |

### Generating / 生成

**Sound warning! 音量警告！**

The `tc_utils.py` is the utility module responsible for the structures shared among all voicebanks, and is *not* supposed to run on its own. Instead,
run the other `.py` files, and the process should start right away. Upon completion, the program raises a short sound, and all the files needed
are placed in the `res` directory.

`tc_utils.py` 是用来整合声库共通内容的功能性模块，*不*应该单独运行，要运行的是其他 `.py` 文件，进度应该立即开始。完成后，程序发出短促音效，所有需要的文件都位于 `res` 目录下。

Most time and calculation are for the frequency table (`.frq` files) generating. If you decide to skip the tables and leave the work for OpenUTaU,
you can add a parameter `save_frq = False` in the `Tc` object definition, and the generating time can be greatly reduced. The downside is that
our built-in correction would not work, and certain audios might be miscalculated (220 Hz -> 440 Hz or so) and sound terrible.

多数时间和计算量都花在生成频率表（`.frq` 文件）上了。如果你想跳过频率表，把计算量都留给 OpenUTaU，可以在 `Tc` 对象的定义中增加参数 `save_frq = False`，
这样就可以极大地减少生成时间。缺点是程序内置的纠正机制没有发挥作用，有的音频可能计算不正确（比如 220 Hz 变成 440 Hz），听感就炸了。

### Installation / 安装

You can zip and rename the `res` folder and follow the regular installing procedure of OpenUTaU. An alternative method is to create a folder under the
`<OpenUTaU install dir>/Singers` directory, and copy everything inside our `res` folder there. If everything worked right, you can find your
precious voicebank in the OpenUTaU singer list. You should really cheer for this massive success!

你可以压缩并重命名 `res` 目录，并遵循 OpenUTaU 通常的安装流程安装它。一种替代方案是在 `<OpenUTaU 安装目录>/Singers` 下新建文件夹，把 `res` 里所有的东西复制过去，
如果一切顺利，那么你珍贵的声库就出现在软件的歌手列表里了。真应该为这么大的成功庆祝一下！

Note that the voicebank is deliberated for **Open**UTaU. Might not work properly on the original UTaU, for the images are PNG format,
and text files are UTF-8 encoded.

注意声库专为 **Open**UTaU 定制，可能不会在原版 UTaU 上正常作用，因为图像都是 PNG 格式，文本都是 UTF-8 编码。

### Tuning / 调校

There should be no difference between regular (hand made) OpenUTaU voicebanks and our voicebanks (except that ours might work a bit worse).

通常（手搓）的 OpenUTaU 声库和咱的应该没有区别（就是咱的效果恐怕差一点）。