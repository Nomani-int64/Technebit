Technebit: an FM-based inorganic OpenUTaU voicebank
======
*锝比特：基于 FM 的无生物 OpenUTaU 音源*

*by Nomani (alias/别名: Nomani_int64 / Nomani-int64)*

## What's inside? / 这里面都是什么？

You might expect an out-of-the-box OpenUTaU voicebank in this GitHub repo, but obviously this isn't the case. You see, I have really wanted
to put together all the resources you might need about this character / voicebank when you do contributions, modifications or fanarts,
though you may have to pick them out from this mess.

你可能会以为这个 GitHub 仓库里面是开箱即用的 OpenUTaU 音源，但是很显然并非如此。我其实很想把关于这个角色/音源所有的资源都整合到一起，
这样其他人做开发、魔改和二创就方便了，就是你可能要从这堆玩意里面自行挑选需要的东西。

Right now we have these subdirectories. **More details can be found in the separate README files.** Most stuff should work fine with Windows 11 25H2,
Python 3.12 and OpenUTaU v0.1.565.0. I have zero idea how multiplatform works, so if you're on other OS's you might have to alter stuff by hand.

现在这里有如下的子目录，**具体信息可查阅各自的说明文件**。多数东西在 Windows 11 25H2、Python 3.12 和 OpenUTaU v0.1.565.0 上应该能用。我完全没接触过多平台开发，
因此如果你用的是其他系统，可能需要徒手修改一下。

- `generator` - The Python program that generates the voicebank. 生成声库的 Python 程序。
- `blender` - 3D Blender model of the character. 角色的 3D Blender 模型。
- `illustration` - Several image files about this character. 有关角色设定的若干图像文件。

## What's special of this voicebank? / 这个声库有什么特别的？

As the title suggests, this is **a voicebank based off FM (frequency modulation) synth**. Long story short, sine functions in sine functions.
It was me tinkering with the [EPSM](https://github.com/Perkka2/EPSM) extension of [FamiStudio](https://github.com/BleuBleu/FamiStudio),
when I found certain parameter combinations that sounds (relatively) like human voices; then I learned a bit about FM synths,
and realized it is somewhat suitable for creating voice. What took place next ... is right in front of you.

如标题所示，这是一个**基于 FM（频率调制）合成器的声库**。简单来说，就是正弦函数套正弦函数。我在玩 [FamiStudio](https://github.com/BleuBleu/FamiStudio)
的 [EPSM](https://github.com/Perkka2/EPSM) 扩展时，发现特定的参数组合能产生（比较）类似人声的声音，然后了解了一下 FM 合成，
寻思着这玩意某种意义上还挺适合合成人声的。接下来发生的事情……就都在你眼前了。

There's one thing to clarify, though, that FM synths here is mostly responsible for the vowel part (including nasals, semi-vowels, stuff like that).
I cannot find a method to FM noises, so instead I introduced ready-made white noises and used parametric filters to frame its spectrum
so consonants sound right. The FM results also need some filters so they won't sound too harsh.

但是有一点有必要澄清一下，FM 合成在这里基本上就是负责元音（以及鼻音、半元音等等类似的东西）。我没找着能频率调制噪声的办法，因此引入了现成的白噪声，
用参数滤波器框定其频谱，这样就有了能听的辅音。而 FM 的结果也需要滤波一下，免得听起来太刺耳。

Technebit is, designed to be, an AI robot. I think this method of voice is unexpectedly suitable alongside their playful appearance,
and have hoped you all to like and take care of them.

锝比特，设定上，是个 AI 机器人。我感觉这种声音格外适合其有趣的形象，希望你们也会喜欢和关照。

## What can I do with it? / 我能拿它做什么呢？

Voicebanks just bank the voices, and so do other assets. I'm really open about the usage, but just to clarify the boundaries and avoid
stuff we wouldn't expect, I suggest [**MIT License**](https://mit-license.org/) for the program part (all files ending with `.py`), and
[**CC0 1.0 Universal**](https://creativecommons.org/publicdomain/zero/1.0/) for non-program assets (including the generated product of programs).

声库就负责库库发声，别的东西同理。我对这些东西的使用没什么意见，不过为了明确边界和避免不必要的麻烦，我给程序部分（所有 `.py` 结尾的文件）分派 [**MIT 许可**](https://mit-license.org/)，
给非程序的资源（包括程序生成的结果）分派 [**CC0 1.0 通用协议**](https://creativecommons.org/publicdomain/zero/1.0/)。

In addition, since the voicebank has to be generated before installed, I suggest redistribute the product along with your modification to the programs
(if there is any). And there is a [**Chinese group public guideline**](https://utauchn.huijiwiki.com/wiki/%E5%85%AC%E5%85%B1%E8%A7%84%E7%BA%A6) that serves
as a baseline. If there's any conflict, then **the platform rules come first.**

此外，因为声库得先生成出来才能用，如果你需要再分发成品，请连带你对程序做出的修改（若有）一并发布。
另有[**中华组公共规约**](https://utauchn.huijiwiki.com/wiki/%E5%85%AC%E5%85%B1%E8%A7%84%E7%BA%A6)作为底线，但如果发生冲突，则**平台规则优先**。

## Any problems? / 有问题？

If you've spotted any major problems within the files and programs, please raise issues within this repo. My public online activities are mostly on Bilibili,
you can find me on [my account](https://space.bilibili.com/523568350). I might be too lazy to check often, but if I found anything really important,
I will reply as soon as possible.

如果你发现文件和程序有任何重大问题，请在这个仓库上提 issue。我线上的公开活动基本上都在哔哩哔哩，这是[我的账号](https://space.bilibili.com/523568350)。我比较懒可能不会经常查看，
但是如果真有很重要的事情，我将尽快回复。
