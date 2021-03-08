# p4a_lottie_demo

This repository contains an example python-for-android application using the `android.presplash_lottie` option of buildozer, allowing to display  short animation instead of a static image while the application starts.

Lottie is a vector format (hence quite lightweight) documented at http://airbnb.io/lottie/#/.
You can find a lot of neat examples animation of this format at https://lottiefiles.com/

You can design your own (or edit existing ones, provided the author granted such permission), using various tools. Aside the popular (but expensive) [Adobe After Effect](https://lottiefiles.com/plugins/after-effects), you can also use [Synfig](https://www.synfig.org/) (free/open source) which can also export animations as lottie files as of [1.4.0](https://synfig.readthedocs.io/en/latest/releases/stable/1.4.0.html#rendering-and-export).

This project is built using github-actions, so provided a recent enough build happened, you should be able to download the example apk package from the "artifacts" section of [a recent build](https://github.com/tshirtman/p4a_lottie_demo/actions).
