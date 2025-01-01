![Sorting-Copilot](https://cdn.jsdelivr.net/gh/Tsumugii24/Typora-images@main/images/2024%2F04%2F02%2Fa399db1cdc40432c73b6210b36816889-Sorting-Copilot-1a734c.png)

</div>

### <div align="center"><h2>Description</h2></div>

&emsp;&emsp;**Sorting-Copilot** is a Multi-Dimensional Waste Sorting Assistant System based on deep neural networks.



</div>

### <div align="center"><h2>Demonstration</h2></div>

&emsp;&emsp;You can easily and directly experience the project demo online on `HuggingFace` now and compare the effects of different models on waste classification.

![image-20250101204733275](https://cdn.jsdelivr.net/gh/Tsumugii24/Typora-images@main/images/2025/01/01/01b17b2c994636d72aaf590b1139a6de-image-20250101204733275-b81995.png)



</div>

### <div align="center"><h2>Quick Start</h2></div>

<details open>
    <summary><h4>Local Installation</h4></summary>


​    I strongly recommend you to use **`conda`** as your local environment. Both `Anaconda` and `miniconda` is OK!


1. Create a virtual **`conda`** environment for our demo 😆

```bash
$ conda create -n sort python==3.8  # sort is the name of your conda env
$ conda activate sort
```

2. Install essential **requirements** by run the following command in the CLI 😊

```bash
$ git clone https://github.com/Tsumugii24/Sorting-Copilot && cd Sorting-Copilot
$ pip install -r requirements.txt
```

3. Download `models` that have already been trained properly

```
$ python download_trained_model.py
```

​	It is recommended because the script  `download_trained_model.py` can automatically download model files for you 🤗

​    However, if there is something wrong with your internet connection, you can also try to download manually from 🤗

- [x] Google Drive  https://drive.google.com/drive/folders/1-H4nN8viLdH6nniuiGO-_wJDENDf-BkL?usp=sharing

![image-20250101210706800](https://cdn.jsdelivr.net/gh/Tsumugii24/Typora-images@main/images/2025/01/01/aeb73bfcdd93f794a542cbc7f8510ff8-image-20250101210706800-b12078.png)

- [x] `HuggingFace` Model Card  [Tsumugii/Sorting-Copilot at main](https://huggingface.co/Tsumugii/Sorting-Copilot/tree/main)

![image-20250101213235906](https://cdn.jsdelivr.net/gh/Tsumugii24/Typora-images@main/images/2025/01/01/80b9d2a4cb4b7ff337bfed514cf844c3-image-20250101213235906-465116.png)

   Choose one of the ways above to download your preferred models and remember to put them under the `Sorting-Copilot/models` directory 😉



</details>

<details open>
	<summary><h4>Run</h4></summary>

```bash
$ python app.py
```

Now, if everything goes smoothly, your default browser will open automatically

and `Gradio` is running on local url:  http://127.0.0.1:7860

</details>



</div>

### <div align="center"><h2>Contact</h2></div>

*Feel free to contact by opening GitHub issues or directly send me a mail if you have any questions about the project.* 👻

​	  											

