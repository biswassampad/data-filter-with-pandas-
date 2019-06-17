{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   #                   Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  \\\n",
      "0  1              Bulbasaur  Grass  Poison  45      49       49       65   \n",
      "1  2                Ivysaur  Grass  Poison  60      62       63       80   \n",
      "2  3               Venusaur  Grass  Poison  80      82       83      100   \n",
      "3  3  VenusaurMega Venusaur  Grass  Poison  80     100      123      122   \n",
      "4  4             Charmander   Fire     NaN  39      52       43       60   \n",
      "\n",
      "   Sp. Def  Speed  Generation  Legendary  \n",
      "0       65     45           1      False  \n",
      "1       80     60           1      False  \n",
      "2      100     80           1      False  \n",
      "3      120     80           1      False  \n",
      "4       50     65           1      False  \n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv('pokemon_data.csv')\n",
    "#df_xlsx = pd.read_excel('pokemon_data.xlsx')\n",
    "\n",
    "#print(df_xlsx.head(3))\n",
    "#print(df.head(3))\n",
    "\n",
    "df = pd.read_csv('pokemon_data.txt',delimiter= '\\t')\n",
    "print(df.head(5))"
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
   "display_name": "Python 3",
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
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
