import matplotlib.pyplot as plt
import numpy as np

# user num = 50
labels = ['2%', '4%', '6%', '8%', '10%']
unl_fr = [997 , 997, 997, 997, 997  ]

unl_hess_r = [17*997/20/50000*100 +997/20, 30*997/20/50000*100 +997/20, 26*997/20/50000*100 +997/20 , 13*997/20/50000*100 +997/20, 32*997/20/50000*100 +997/20 ]
unl_br = [17*997/20/50000*100,           10*997/20/50000*100   , 26*997/20/50000*100, 31*997/20/50000*100, 38*997/20/50000*100]

unl_vib = [40*997/20/50000*100*2,          63*997/20/50000*100*2     , 50*997/20/50000*100*2, 86*997/20/50000*100*2, 50*997/20/50000*100*2]
unl_self_r=[47*997/20/50000*100*2,       70*997/20/50000*100*2      , 52*997/20/50000*100*2, 82*997/20/50000*100*2, 100*997/20/50000*100*2]



x = np.arange(len(labels))  # the label locations
width = 0.6  # the width of the bars
# no_noise = np.around(no_noise,0)
# samping = np.around(samping,0)
# ldp = np.around(ldp,0)


plt.figure()
#plt.subplots(figsize=(8, 5.3))
#plt.bar(x - width / 2 - width / 8 + width / 8, unl_fr, width=0.168, label='Retrain', color='dodgerblue', hatch='/')
plt.bar(x - width / 2 - width / 8 + width / 8 , unl_br, width=0.168, label='VBU', color='orange', hatch='\\')
plt.bar(x - width / 8 - width / 16, unl_vib, width=0.168, label='MCFU$_{w}$', color='palegreen', hatch='/')
plt.bar(x + width / 8, unl_self_r, width=0.168, label='MCFU$_{w/o}$', color='g', hatch='x')
plt.bar(x + width / 2 - width / 8 + width / 16, unl_hess_r, width=0.168, label='HBFU', color='tomato', hatch='-')


# plt.bar(x - width / 2.5 ,  unl_br, width=width/3, label='VBU', color='orange', hatch='\\')
# plt.bar(x,unl_self_r, width=width/3, label='RFU-SS', color='g', hatch='x')
# plt.bar(x + width / 2.5,  unl_hess_r, width=width/3, label='HBU', color='tomato', hatch='-')


# Add some text for labels, title and custom x-axis tick labels, etc.
plt.ylabel('Running Time (s)', fontsize=20)
# ax.set_title('Performance of Different Users n')
plt.xticks(x, labels, fontsize=20)
# ax.set_xticklabels(labels,fontsize=15)

my_y_ticks = np.arange(0, 66.1, 10)
plt.yticks(my_y_ticks, fontsize=20)
# ax.set_yticklabels(my_y_ticks,fontsize=15)

plt.legend(loc='upper left', fontsize=20)
plt.xlabel('$\it{EDR}$' ,fontsize=20)
# ax.bar_label(rects1, padding=1)
# ax.bar_label(rects2, padding=3)
# ax.bar_label(rects3, padding=3)

plt.tight_layout()

plt.rcParams['figure.figsize'] = (2.0, 1)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['figure.subplot.left'] = 0.11
plt.rcParams['figure.subplot.bottom'] = 0.08
plt.rcParams['figure.subplot.right'] = 0.977
plt.rcParams['figure.subplot.top'] = 0.969
plt.savefig('cifar100_rt_er_bar.png', dpi=200)
plt.show()
