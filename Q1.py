{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "N = int(input(\"N\"))\n",
    "check = True\n",
    "while check == True:\n",
    "    values_N = list(map(str, input(\"Size\").split()))\n",
    "    print(len(values_N))\n",
    "    if len(values_N)==N: check = False\n",
    "\n",
    "M = int(input(\"M\"))\n",
    "check = True\n",
    "while check == True:\n",
    "    values_M = list(map(str, input(\"Size\").split()))\n",
    "    if len(values_M)==M: check = False\n",
    "\n",
    "values_num_n = []\n",
    "values_num_m = []\n",
    "\n",
    "for i in values_N:\n",
    "    num = 0\n",
    "    if i == \"M\": \n",
    "        values_num_n.append(num)\n",
    "    else:\n",
    "        num = len(i)-1\n",
    "        if i[-1]==\"S\": num*=-1\n",
    "\n",
    "for i in values_M:\n",
    "    num = 0\n",
    "    if i == \"M\": \n",
    "        values_num_m.append(num)\n",
    "    else:\n",
    "        num = len(i)-1\n",
    "        if i[-1]==\"S\": num*=-1\n",
    "\n",
    "values_num_m.sort()\n",
    "\n",
    "for i in values_num_m:\n",
    "    if values_num_n[-1*i] >= values_num_m[-1*i]:\n",
    "        values_num_n.remove(-1*i)\n",
    "        values_num_m.remove(-1*i)\n",
    "\n",
    "if len(values_num_m) ==0: print(\"Yes\")\n",
    "else: print(\"No\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.9.7 ('base')",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "750f7130a0ed5887341392c7bdb5265c945b64bfd064bdaec7ae8d3d01e224ab"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
