import pygame
from MeleeEnemy import *
from RangedEnemy import *


class Levels():
    def __init__(self):
        C1 = {'melee':[1,3], 'ranged':[0,0], 'skell':[0,0], 'zombi':[0,0],
              'meleer':[0,0], 'meleeg':[0,0], 'nox':[0,0], 'stella':[0,0]}

        C2 = {'melee':[3,3], 'ranged':[1,2], 'skell':[0,0], 'zombi':[0,0],
             'meleer':[0,0], 'meleeg':[0,0], 'nox':[0,0], 'stella':[0,0]}

        C3 = {'melee':[2,3], 'ranged':[3,2], 'skell':[0,0], 'zombi':[0,0],
             'meleer':[0,1], 'meleeg':[0,0], 'nox':[0,0], 'stella':[0,0]}
        self.L1 = [C1, C2, C3]

        C4 = {'melee':[1,0], 'ranged':[1,2], 'skell':[0,0], 'zombi':[0,0],
              'meleer':[2,3], 'meleeg':[0,0], 'nox':[0,0], 'stella':[0,0]}

        C5 = {'melee':[0,0], 'ranged':[1,2], 'skell':[0,0], 'zombi':[1,4],
             'meleer':[3,1], 'meleeg':[0,0], 'nox':[0,0], 'stella':[0,0]}

        C6 = {'melee':[0,0], 'ranged':[1,0], 'skell':[1,3], 'zombi':[4,3],
             'meleer':[0,0], 'meleeg':[0,0], 'nox':[0,0], 'stella':[0,0]}
        self.L2 = [C4, C5, C6]

        C7 = {'melee':[1,0], 'ranged':[1,0], 'skell':[1,2], 'zombi':[1,1],
              'meleer':[1,2], 'meleeg':[1,2], 'nox':[0,0], 'stella':[0,0]}

        C8 = {'melee':[0,0], 'ranged':[3,0], 'skell':[2,4], 'zombi':[0,0],
             'meleer':[2,0], 'meleeg':[1,1], 'nox':[0,0], 'stella':[0,1]}

        C9 = {'melee':[0,0], 'ranged':[0,0], 'skell':[0,0], 'zombi':[0,0],
             'meleer':[0,0], 'meleeg':[0,0], 'nox':[1,0], 'stella':[0,0]}
        self.L3 = [C7, C8, C9]
        self.levels = [self.L1, self.L2, self.L3]

    def setup_enemies(self, l, c, w, m_enemy_List, r_enemy_List, enemy_Group, health_Group):
        melee = self.levels[l][c].get('melee')[w]
        zombi = self.levels[l][c].get('zombi')[w]
        ranged = self.levels[l][c].get('ranged')[w]
        skelli = self.levels[l][c].get('skell')[w]
        meleer = self.levels[l][c].get('meleer')[w]
        meleeg = self.levels[l][c].get('meleeg')[w]
        nox = self.levels[l][c].get('nox')[w]
        stella = self.levels[l][c].get('stella')[w]
        for i in range(melee):
            m_enemy_List.append(MeleeEnemy(2000+150*i))
        for i in range(zombi):
            m_enemy_List.append(Zombi(2000+150*(i+melee)))
        for i in range(meleer):
            m_enemy_List.append(MeleeEnemyR(2000+150*(i+melee+zombi)))
        for i in range(meleeg):
            m_enemy_List.append(MeleeEnemyG(2000+150*(i+melee+zombi+meleer)))
        for i in range(nox):
            m_enemy_List.append(Nox(2000+150*(i+melee+zombi+meleer+meleeg)))

        for i in range(ranged):
            r_enemy_List.append(RangedEnemy(2100+150*i))
        for i in range(skelli):
            r_enemy_List.append(Skelli(2100+150*(i+ranged)))
        for i in range(stella):
            r_enemy_List.append(Stella(2100+150*(i+ranged+skelli)))

        for en in m_enemy_List:
            enemy_Group.add(en)
            health_Group.add(en.healthbar)
        for en in r_enemy_List:
            enemy_Group.add(en)
            health_Group.add(en.healthbar)
