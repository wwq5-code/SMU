

import numpy as np
import matplotlib.pyplot as plt

epsilon = 3
beta = 1 / epsilon


x=[1, 2, 3, 4, 5]
# validation_for_plt =[97,95.8600, 94.9400, 93.5400, 93.2400]
# attack_for_plt=[0, 0.3524, 0, 0.1762, 0.1762]
# basic_for_plt=[99.8, 99.8, 99.8, 99.8, 99.8]

labels = ['20%', '40%', '60%', '80%', '100%']
unl_org_0=[9.42,  9.42, 9.42, 9.42, 9.42]
unl_org = [94.07, 80.92, 85.703, 86.48, 77.69]

unl_hess_r = [4.951407, 4.9514073, 4.951407, 4.951407, 4.951407]
unl_vbu = [52.9582, 52.9582, 52.9582, 52.9582, 52.9582]


unl_ss_w = [3.5399, 4.53438, 4.291, 5.2954, 6.18831]
unl_ss_wo = [3.87029, 3.9979, 5.0408, 5.3503, 7.10648]



plt.figure(figsize=(5.5, 5.3))
l_w=5
m_s=15
marker_s = 3
markevery=1
#plt.figure(figsize=(8, 5.3))
#plt.plot(x, unl_fr, color='blue', marker='^', label='Retrain',linewidth=l_w, markersize=m_s)
plt.plot(x, unl_ss_w, linestyle='-', color='b', marker='o', fillstyle='none', markevery=markevery,
         label='SMU$_{w}$', linewidth=l_w, markersize=m_s, markeredgewidth=marker_s)

#plt.plot(x, unl_ss_w, color='g',  marker='*',  label='SMU$_{w}$',linewidth=l_w, markersize=m_s)
plt.plot(x, unl_ss_wo, linestyle='--', color='g',  marker='s', fillstyle='none', markevery=markevery,
         label='SMU$_{w/o}$',linewidth=l_w, markersize=m_s, markeredgewidth=marker_s)

plt.plot(x, unl_vbu, linestyle=':', color='r',  marker='^', fillstyle='none', markevery=markevery,
         label='VBU', linewidth=l_w,  markersize=m_s, markeredgewidth=marker_s)

plt.plot(x, unl_hess_r, linestyle='-.', color='k',  marker='D', fillstyle='none', markevery=markevery,
         label='HBFU',linewidth=l_w, markersize=m_s, markeredgewidth=marker_s)



#plt.plot(x, unl_vibu, color='silver',  marker='d',  label='VIBU',linewidth=4,  markersize=10)

# plt.plot(x, y_sa03, color='r',  marker='2',  label='AAAI21 A_acc, pr=0.3',linewidth=3, markersize=8)
# plt.plot(x, y_sa05, color='darkblue',  marker='4',  label='AAAI21 A_acc, pr=0.5',linewidth=3, markersize=8)
# plt.plot(x, y_ma03, color='darkviolet',  marker='3',  label='FedMC A_acc, pr=0.3',linewidth=3, markersize=8)
# plt.plot(x, y_ma05, color='cyan',  marker='p',  label='FedMC A_acc, pr=0.5',linewidth=3, markersize=8)


plt.grid()
leg = plt.legend(fancybox=True, shadow=True)
# plt.xlabel('Malicious Client Ratio (%)' ,fontsize=16)
plt.ylabel('Mutual Information' ,fontsize=24)
my_y_ticks = np.arange(0, 61, 10)
plt.yticks(my_y_ticks, fontsize=20)
plt.xlabel('$\it{SR}$', fontsize=20)

plt.xticks(x, labels, fontsize=20)
# plt.title('CIFAR10 IID')
plt.title('(a) Privacy Preservation', fontsize=24)
plt.legend(loc='best', fontsize=20)
plt.tight_layout()
#plt.title("MNIST")
plt.rcParams['figure.figsize'] = (2.0, 1)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['figure.subplot.left'] = 0.11
plt.rcParams['figure.subplot.bottom'] = 0.08
plt.rcParams['figure.subplot.right'] = 0.977
plt.rcParams['figure.subplot.top'] = 0.969
plt.savefig('cifar100_mi_epsilon_curve.png', dpi=200)
plt.show()