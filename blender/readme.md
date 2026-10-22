Technebit-blender: nothing special
======
*锝比特-Blender：没什么特别的*

*by Nomani (alias/别名: Nomani_int64 / Nomani-int64)*

Please open the `.blend` file with Blender 5.2+. External resources should be packed inside, but just in case they don't work properly, you can find a
copy of all relevant files in the `textures` subfolder.

请用 Blender 5.2 或更新版打开 `.blend` 文件。外部资源应该打包在工程文件里，但是以防其损坏，`textures` 子目录里还有一份拷贝。

The only thing I think worth mentioning is the shape keys in the face (screen) mesh, including `MouthWidth` and `MouthHeight`. To apply a
quick (yet very inaccurate) animation to them, please run the Python script in the same folder with parameters:

我感觉有必要提的东西就是脸（屏幕）网格上的形态键，包括 `MouthWidth` 和 `MouthHeight`。要给它们快速（而极其不精确地）应用动画，请带参数运行同一目录下的 Python 脚本：

```shell
python blender/anim.py path/to/audio.wav output
```

The second parameter is the audio to be played, or 'said' by the robot, and the last is the output file prefix. After processing, you get two
'audio' files, `output1.wav` and `output2.wav`, which is **not for playing**, but as numeric samples. You can add a blank object in your
Blender project, add keyframes to two of its position channels, switch to curve editor and select the Sound to Sample command. Here you can
load the sample 'audios' and bake their waveforms into motion data. Then use drivers to bind these data to the shape keys and it's done.
(I actually forgot which to which, you can try both and choose whichever works better!)

第二个参数就是要播放，或者说让机器人“说”的音频，最后一个是输出文件的前缀。处理过后，会得到两个“音频”文件 `output1.wav` 和 `output2.wav`，这些**不是用来播放的**，
而是作为数值样本。在你的 Blender 项目中添加一个空物体，在其中两个位置通道上打关键帧，切换到曲线编辑器并选择“音频到采样”选项，这样你就可以加载采样“音频”
将其波形烘焙为运动数据。然后，用驱动器将这些数据绑定到形态键上就可以了。（其实我忘了哪个对哪个了，你可以都试试看，选择效果比较好的就行了！）