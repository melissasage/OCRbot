# OCRbot

OCRbot is a Mastodon (and compatible, such as Pleroma) bot that uses OCR to automatically generate text descriptions of images. It reads the image and outputs what it thinks is the text contained, using [tesseract](https://github.com/tesseract-ocr/tesseract). **It requires Python 3.**

![Screenshot of OCRbot in action](https://lynnesbian.space/res/ceres/sshot_2019-02-21_at_14-41-06-1550724066.png)

## Working Example

A working version of OCRbot can be found [here](https://fedi.lynnesbian.space/@OCRbot). I'll always run the latest version, and the instance hosting it has a much higher character limit than Mastodon's default of 500 or Pleroma's default of 5000 (specifically, it has a limit of 65535 chars). If you'd like to run your own version that works differently (for example, maybe you want a version that works with Japanese text instead, or a version that uses a different OCR engine), then you're free to fork and modify!

## Installation
### Tesseract (Required)

- Debian/Ubuntu: `sudo apt install tesseract-ocr`
- Arch Linux: `sudo pacman -Syu tesseract tesseract-data-eng`

#### What about the higher quality data packs?

According to [tesseract's GitHub wiki](https://github.com/tesseract-ocr/tesseract/wiki/Data-Files#updated-data-files-for-version-400-september-15-2017):
> Most users will want `tessdata_fast` and that is what will be shipped as part of Linux distributions. `tessdata_best` is for people willing to trade a lot of speed for slightly better accuracy.

With the setup I'm using, I really can't afford to use much more processing power just for "slightly better accuracy". Additionally, most Linux distributions only ship the `fast` set, which makes obtaining the `best` set an extra step. I haven't tested how much better `fast` is than `best`, but given that distributions like Arch and Debian deemed `fast` good enough to be the only package available, I'm inclinded to suspect that this is a case of diminishing returns, and that it's not worth the extra effort of obtaining these files, as well as the extra CPU usage required to use them.

### OCRbot (Required)

```
git clone https://github.com/Lynnesbian/OCRbot/
cd OCRbot
pip3 install -r requirements.txt
```

## Running OCRbot
Copy or rename `config.sample.json` to `config.json`, and edit the settings as you wish. Most importantly, make sure you choose the instance your OCRbot account will post from. Then, run `main.py` and log in with the account you'd like OCRbot to post from. Finally, run `reply.py` and OCRbot will take care of the rest.

You can use something like systemd or SysVinit to manage running `reply.py` for you. I've provided an example systemd script [here](systemd-example.service). It requires some editing (to specify where your OCRbot folder is located, and to specify the user to run it as -- *don't run it as root*), and then you simply need to
```
sudo mv systemd-example.service /etc/systemd/system/OCRbot.service
sudo systemctl start OCRbot
```
You may also `sudo systemctl enable OCRbot` if you want it to start on boot.

## Caveats
OCRbot is *not* designed to replace captions, merely to supplement them. It works best with plain black text on a plain white background. For example, PDF scans and Wikipedia screenshots will work great, but handwriting and distorted text won't. It will almost always fail (at least partially) for:
- Anything using handwriting
- Anything that's not in English (although I'm planning on fixing this)
- Text that is skewed, rotated, stretched, or otherwise distorted
- Heavily compressed images
- Text with layouts more complex than this page
- WordArt
- Unusual fonts
- Videos and GIFs
- Very large or very small text
- Text on a complex background

Additionally, OCRbot may sometimes fail to find images due to federation issues. This is a known bug, and I am currently looking into solving it, but it will never be completely solved. If any instances have blocked fedi.lynnesbian.space (or vice versa), the post will not make it to my instance, and OCRbot won't be able to find it.

So in short, please caption your images. Don't rely on OCRbot.

## Donating
Donations can be provided via [Patreon](https://patreon.com/lynnesbian) [LiberaPay](https://liberapay.com/lynnesbian) (recurring), [PayPal](https://paypal.me/lynnesbian) (singular), or [Ko-fi](https://ko-fi.com/lynnesbian) (singular). Don't feel obligated to donate!

## License
Copyright (C)2019 Lynnesbian (https://fedi.lynnesbian.space/@lynnesbian)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

The full text of the license is provided under the name "LICENSE" in the root directory of this repository.
