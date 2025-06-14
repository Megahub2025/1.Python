{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOclOYsrRpj2AVv9m0IceTe",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Megahub2025/1.Python/blob/main/my_class_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "zkHrzYr39w7n"
      },
      "outputs": [],
      "source": [
        "#create class with multi functions\n",
        "class My_Class:\n",
        "\n",
        "#function to list out AI subfields\n",
        "  def SubfieldsInAI():\n",
        "    AI_list=['Machine Learning','Neural Networks','Vision','Robotics','Speech processing','Natural Language Processing']\n",
        "    for list in AI_list:\n",
        "      print(list)\n",
        "\n",
        "#function that checks whether the given number is Odd or Even\n",
        "  def OddEven():\n",
        "    getinput=int(input(\"Enter a number: \"))\n",
        "    if (getinput%2==0):\n",
        "      result=print(getinput,\"is even\")\n",
        "      return result\n",
        "    else:\n",
        "      result=print(getinput,\"is odd\")\n",
        "      return result\n",
        "\n",
        "#function that tells elegibility of marriage for male and female according to their age limit : 21 for male and 18 for female\n",
        "  def marriage_elegibility():\n",
        "    getgender=str(input(\"Enter your gender: \"))\n",
        "    getage=int(input(\"Enter your age: \"))\n",
        "    if(getgender==\"female\" and getage>=18):\n",
        "      result=print(\"You are eligible\")\n",
        "      return result\n",
        "    elif(getgender==\"male\" and getage>=21):\n",
        "      result=print(\"You are eligible\")\n",
        "      return result\n",
        "    else:\n",
        "      result=print(\"You are not eligible\")\n",
        "      return result\n",
        "\n",
        "#function to calculate the percentage of your 10th mark\n",
        "  def calculate_percentage():\n",
        "# Input marks for 5 subjects\n",
        "    marks = [ ]\n",
        "    for i in range(1, 6):\n",
        "      mark = float(input(f\"Subject {i}: \"))\n",
        "      marks.append(mark)\n",
        "# Calculate total and percentage\n",
        "    total_marks = sum(marks)\n",
        "    percentage = (total_marks / 500) * 100\n",
        "    print(\"Total Marks: \",total_marks)\n",
        "    print(\"Percentage: \",percentage)\n",
        "\n",
        "#calculate area and perimeter or triangle using class and function\n",
        "  def triangle_Calc():\n",
        "    calc=input(\"Calculate Area or Perimeter?: \")\n",
        "    if (calc==\"Area\"):\n",
        "      Height=int(input(\"Height: \"))\n",
        "      Breadth=int(input(\"Breadth:\"))\n",
        "      Area=(Height*Breadth)/2\n",
        "      area_result=print(\"Area of Triangle: \",Area)\n",
        "      return(area_result)\n",
        "    elif (calc==\"Perimeter\"):\n",
        "      Height1=int(input(\"Height1: \"))\n",
        "      Height2=int(input(\"Height2: \"))\n",
        "      Breadth=int(input(\"Breadth:\"))\n",
        "      Perimeter=Height1+Height2+Breadth\n",
        "      peri_result=print(\"Perimeter of Triangle: \",Perimeter)\n",
        "      return(peri_result)\n",
        "    else:\n",
        "      no_result=print(\"Invalid choice. Please enter 'Area' or 'Perimeter'.\")\n",
        "      return(no_result)\n",
        "\n",
        "\n"
      ]
    }
  ]
}