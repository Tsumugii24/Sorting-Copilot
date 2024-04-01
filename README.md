![Sorting-Copilot](https://cdn.jsdelivr.net/gh/Tsumugii24/Typora-images@main/images/2024%2F04%2F02%2Fa399db1cdc40432c73b6210b36816889-Sorting-Copilot-1a734c.png)

</div>

### <div align="center"><h2>Description</h2></div>

&emsp;&emsp;**Sorting-Copilot** is a Multi-Dimensional Waste Sorting Assistant System based on deep neural networks.



</div>

### <div align="center"><h2>Demonstration</h2></div>

&emsp;&emsp;You can easily and directly experience the project demo online on `HuggingFace` now and compare the effects of different models on waste classification.

Click here for Online Experience 👉 [Lesion-Cells DET - a Hugging Face Space by Tsumugii](https://huggingface.co/spaces/Tsumugii/lesion-cells-det)

![4a7077aee8660255dd7e08ca4cdd3680-demo-daa408.gif](https://github.com/Tsumugii24/Typora-images/blob/main/images/2023/11/14/4a7077aee8660255dd7e08ca4cdd3680-demo-daa408.gif?raw=true)



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

- [ ] Google Drive  https://drive.google.com/drive/folders/1-H4nN8viLdH6nniuiGO-_wJDENDf-BkL?usp=sharing

![b5fd2a2773cff7b112c2b3328e172bd3-image-20231114005824778-df9e54.png](https://github.com/Tsumugii24/Typora-images/blob/main/images/2023/11/14/b5fd2a2773cff7b112c2b3328e172bd3-image-20231114005824778-df9e54.png?raw=true)

- [ ] `HuggingFace` Model Card  https://huggingface.co/Tsumugii/lesion-cells-det/tree/main

![78c42a6194428efa79ed499f9401e823-image-20240106191732142-b3de11.png](https://github.com/Tsumugii24/Typora-images/blob/main/images/2024/01/06/78c42a6194428efa79ed499f9401e823-image-20240106191732142-b3de11.png?raw=true)

   Choose one of the ways above to download your preferred models and remember to put them under the `project-root/models` directory 😉



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

*Feel free to contact me through GitHub issues or directly send me a mail if you have any questions about the project.* 👻



<div align="center"><h4>Here is my email address 👉 jsf002016@gmail.com</h4></div>

​	  											

