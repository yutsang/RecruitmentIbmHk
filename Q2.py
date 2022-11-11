{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "N = int(input(\"N\"))\n",
    "allValid = True\n",
    "errorCodes = []\n",
    "\n",
    "for i in range(N):\n",
    "    line = input().split()\n",
    "    if len(line) == 2:\n",
    "        continue\n",
    "    else:\n",
    "        allValid = False\n",
    "        errorCodes.append(line[-1])\n",
    "\n",
    "if allValid:\n",
    "    print(\"Yes\")\n",
    "else:\n",
    "    print(\"No\")\n",
    "    print(*errorCodes)"
   ]
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
