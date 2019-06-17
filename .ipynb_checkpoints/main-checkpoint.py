{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    #\\tName\\tType 1\\tType 2\\tHP\\tAttack\\tDefense\\tSp. Atk\\tSp. Def\\tSpeed\\tGeneration\\tLegendary\n",
      "0    1\\tBulbasaur\\tGrass\\tPoison\\t45\\t49\\t49\\t65\\t6...                                          \n",
      "1    2\\tIvysaur\\tGrass\\tPoison\\t60\\t62\\t63\\t80\\t80\\...                                          \n",
      "2    3\\tVenusaur\\tGrass\\tPoison\\t80\\t82\\t83\\t100\\t1...                                          \n",
      "3    3\\tVenusaurMega Venusaur\\tGrass\\tPoison\\t80\\t1...                                          \n",
      "4    4\\tCharmander\\tFire\\t\\t39\\t52\\t43\\t60\\t50\\t65\\...                                          \n",
      "5    5\\tCharmeleon\\tFire\\t\\t58\\t64\\t58\\t80\\t65\\t80\\...                                          \n",
      "6    6\\tCharizard\\tFire\\tFlying\\t78\\t84\\t78\\t109\\t8...                                          \n",
      "7    6\\tCharizardMega Charizard X\\tFire\\tDragon\\t78...                                          \n",
      "8    6\\tCharizardMega Charizard Y\\tFire\\tFlying\\t78...                                          \n",
      "9    7\\tSquirtle\\tWater\\t\\t44\\t48\\t65\\t50\\t64\\t43\\t...                                          \n",
      "10   8\\tWartortle\\tWater\\t\\t59\\t63\\t80\\t65\\t80\\t58\\...                                          \n",
      "11   9\\tBlastoise\\tWater\\t\\t79\\t83\\t100\\t85\\t105\\t7...                                          \n",
      "12   9\\tBlastoiseMega Blastoise\\tWater\\t\\t79\\t103\\t...                                          \n",
      "13   10\\tCaterpie\\tBug\\t\\t45\\t30\\t35\\t20\\t20\\t45\\t1...                                          \n",
      "14   11\\tMetapod\\tBug\\t\\t50\\t20\\t55\\t25\\t25\\t30\\t1\\...                                          \n",
      "15   12\\tButterfree\\tBug\\tFlying\\t60\\t45\\t50\\t90\\t8...                                          \n",
      "16   13\\tWeedle\\tBug\\tPoison\\t40\\t35\\t30\\t20\\t20\\t5...                                          \n",
      "17   14\\tKakuna\\tBug\\tPoison\\t45\\t25\\t50\\t25\\t25\\t3...                                          \n",
      "18   15\\tBeedrill\\tBug\\tPoison\\t65\\t90\\t40\\t45\\t80\\...                                          \n",
      "19   15\\tBeedrillMega Beedrill\\tBug\\tPoison\\t65\\t15...                                          \n",
      "20   16\\tPidgey\\tNormal\\tFlying\\t40\\t45\\t40\\t35\\t35...                                          \n",
      "21   17\\tPidgeotto\\tNormal\\tFlying\\t63\\t60\\t55\\t50\\...                                          \n",
      "22   18\\tPidgeot\\tNormal\\tFlying\\t83\\t80\\t75\\t70\\t7...                                          \n",
      "23   18\\tPidgeotMega Pidgeot\\tNormal\\tFlying\\t83\\t8...                                          \n",
      "24   19\\tRattata\\tNormal\\t\\t30\\t56\\t35\\t25\\t35\\t72\\...                                          \n",
      "25   20\\tRaticate\\tNormal\\t\\t55\\t81\\t60\\t50\\t70\\t97...                                          \n",
      "26   21\\tSpearow\\tNormal\\tFlying\\t40\\t60\\t30\\t31\\t3...                                          \n",
      "27   22\\tFearow\\tNormal\\tFlying\\t65\\t90\\t65\\t61\\t61...                                          \n",
      "28   23\\tEkans\\tPoison\\t\\t35\\t60\\t44\\t40\\t54\\t55\\t1...                                          \n",
      "29   24\\tArbok\\tPoison\\t\\t60\\t85\\t69\\t65\\t79\\t80\\t1...                                          \n",
      "..                                                 ...                                          \n",
      "770  700\\tSylveon\\tFairy\\t\\t95\\t65\\t65\\t110\\t130\\t6...                                          \n",
      "771  701\\tHawlucha\\tFighting\\tFlying\\t78\\t92\\t75\\t7...                                          \n",
      "772  702\\tDedenne\\tElectric\\tFairy\\t67\\t58\\t57\\t81\\...                                          \n",
      "773  703\\tCarbink\\tRock\\tFairy\\t50\\t50\\t150\\t50\\t15...                                          \n",
      "774  704\\tGoomy\\tDragon\\t\\t45\\t50\\t35\\t55\\t75\\t40\\t...                                          \n",
      "775  705\\tSliggoo\\tDragon\\t\\t68\\t75\\t53\\t83\\t113\\t6...                                          \n",
      "776  706\\tGoodra\\tDragon\\t\\t90\\t100\\t70\\t110\\t150\\t...                                          \n",
      "777  707\\tKlefki\\tSteel\\tFairy\\t57\\t80\\t91\\t80\\t87\\...                                          \n",
      "778  708\\tPhantump\\tGhost\\tGrass\\t43\\t70\\t48\\t50\\t6...                                          \n",
      "779  709\\tTrevenant\\tGhost\\tGrass\\t85\\t110\\t76\\t65\\...                                          \n",
      "780  710\\tPumpkabooAverage Size\\tGhost\\tGrass\\t49\\t...                                          \n",
      "781  710\\tPumpkabooSmall Size\\tGhost\\tGrass\\t44\\t66...                                          \n",
      "782  710\\tPumpkabooLarge Size\\tGhost\\tGrass\\t54\\t66...                                          \n",
      "783  710\\tPumpkabooSuper Size\\tGhost\\tGrass\\t59\\t66...                                          \n",
      "784  711\\tGourgeistAverage Size\\tGhost\\tGrass\\t65\\t...                                          \n",
      "785  711\\tGourgeistSmall Size\\tGhost\\tGrass\\t55\\t85...                                          \n",
      "786  711\\tGourgeistLarge Size\\tGhost\\tGrass\\t75\\t95...                                          \n",
      "787  711\\tGourgeistSuper Size\\tGhost\\tGrass\\t85\\t10...                                          \n",
      "788  712\\tBergmite\\tIce\\t\\t55\\t69\\t85\\t32\\t35\\t28\\t...                                          \n",
      "789  713\\tAvalugg\\tIce\\t\\t95\\t117\\t184\\t44\\t46\\t28\\...                                          \n",
      "790  714\\tNoibat\\tFlying\\tDragon\\t40\\t30\\t35\\t45\\t4...                                          \n",
      "791  715\\tNoivern\\tFlying\\tDragon\\t85\\t70\\t80\\t97\\t...                                          \n",
      "792  716\\tXerneas\\tFairy\\t\\t126\\t131\\t95\\t131\\t98\\t...                                          \n",
      "793  717\\tYveltal\\tDark\\tFlying\\t126\\t131\\t95\\t131\\...                                          \n",
      "794  718\\tZygarde50% Forme\\tDragon\\tGround\\t108\\t10...                                          \n",
      "795  719\\tDiancie\\tRock\\tFairy\\t50\\t100\\t150\\t100\\t...                                          \n",
      "796  719\\tDiancieMega Diancie\\tRock\\tFairy\\t50\\t160...                                          \n",
      "797  720\\tHoopaHoopa Confined\\tPsychic\\tGhost\\t80\\t...                                          \n",
      "798  720\\tHoopaHoopa Unbound\\tPsychic\\tDark\\t80\\t16...                                          \n",
      "799  721\\tVolcanion\\tFire\\tWater\\t80\\t110\\t120\\t130...                                          \n",
      "\n",
      "[800 rows x 1 columns]\n"
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
    "df = pd.read_csv('pokemon_data.txt',delimeter= '\\t')\n",
    "print(df)"
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
