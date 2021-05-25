import numpy as np 
import matplotlib.pyplot as plt



def plot_data(data,tit = "random"):
    for curve in data:
        plt.plot(curve)
    plt.title(tit)
    plt.show()

def append_data_sets_to_one(s1,s2,s3,s4):
    quad = [s1,s2,s3,s4]
    master_list = []
    for dset in quad:
        for point in dset:
            master_list.append(point)
    return master_list






if __name__=="__main__":
    # set1 = np.load("W2/C5/NW/210518143336Realtest0.npy")
    # set2 = np.load("W2/C5/NW/210518143336Realtest1.npy")
    # set3 = np.load("W2/C5/NW/210518143336Realtest2.npy")
    # set4 = np.load("W2/C5/NW/210518143336Realtest3.npy")

    # # plot_data(set1)
    # # plot_data(set2)
    # # plot_data(set3)
    # # plot_data(set4)

    # print ("appending sets together")
    # quad_data = append_data_sets_to_one(set1,set2,set3,set4)
    # plot_data(quad_data)
    # labels = np.ones(len(quad_data))
    # np.save("good_curves",quad_data)
    # np.save("good_curves_labels",labels)

    set1 = np.load("W2/A3/NW/210507132618Fulltest_1.npy")  #<===has bad data
    set2 = np.load("W2/E4/NW/210520160533Fulltest_0.npy")
    set3 = np.load("W2/A4/NW/210507152541FullTests_2.npy")  #<===has bad data
    set4 = np.load("W2/A4/NW/210507160454FullTests_3.npy")  #<===has bad data
    # print(len(set4))
    # plot_data(set1[231:],"set1")
    # plot_data(set2[40:],"set2")
    # plot_data(set3[10:],"set3")
    # plot_data(set4[10:],"set4")
    quad_data = append_data_sets_to_one(set1[231:],set2[40:],set3[10:],set4[10:])
    plot_data(quad_data)
    labels_bad = np.zeros(len(quad_data))
    np.save("bad_curves",quad_data)
    np.save("bad_curves_labels",labels_bad)



