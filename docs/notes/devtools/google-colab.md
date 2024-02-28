# Google Colab

[Google Colab](https://colab.research.google.com/) enables the remote development and execution of Python programs in the cloud, instead of on your local computer.

A Colab notebook document is essentially a Python notebook in Google Drive. These notebook documents contain "code cells" and "text cells". In the code cells we write Python. In the text cells we can write in Markdown (see this [Markdown Cheat Sheet](https://www.markdownguide.org/basic-syntax/) for more details).

Here are more resources for learning how to use Colab:

  + [Intro to Colab Video](https://www.youtube.com/watch?v=inN8seMm7UI)
  + [Welcome to Colab](https://colab.research.google.com/notebooks/intro.ipynb#)
  + [Overview of Colab Features Notebook](https://colab.research.google.com/notebooks/basic_features_overview.ipynb)
  + [Using Colab with GitHub](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)

## Colab Notebooks vs Local Development

Colab is a ground-breaking new tool, but still has limitations, primarily in the areas of security, flexibility, and reproducibility. 

Colab Notebook Advantages:
  + Minimal learning curve
  + High degree of visibility and shareability
  + Effective presentation when code mixed with markdown and data visualizations
  + Potential for GPU / TPU processing power

Colab Notebook Disadvantages:
  + Can only write and execute Python code, not other languages
  + Harder to secure credentials and environment variables
  + Minimal processing power and parallel processing capabilities by default (excluding GPU / TPU)
  + Relatively low degree of customization
  + Unable to run certain kinds of apps, like web apps written in the Flask framework

Local Development Advantages:
  + Can write and execute code written in many different languages and frameworks
  + Greater ability to secure credentials and environment variables
  + Greater degree of customization / control
  + Greater privacy (not managed by Google)
  + More processing power and parallel processing capabilities (excluding GPU / TPU)

Local Development Disadvantages:
  + Steeper learning curve, likely many tools to learn
  + Not as easily shareable, unless pushing code to GitHub or a remote server
  
