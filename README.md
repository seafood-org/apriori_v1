# Implementation of the Apriori Algorithm in Spark

> Chiyi, Zhang. 20981418. czhangdx@connect.ust.hk
>
> Junlang, Ye. 20986482. jyeaq@connect.ust.hk
>
> Linni, Xie. 21003158. lxieaz@connect.ust.hk
>
> Maosen, HUANG. 21003067. mhuangaz@connect.ust.hk



## Abstract

This study explores the domain of Frequent Itemset Mining and presents the implementation of a parallel Apriori algorithm on the Spark distributed computing platform. The traditional Apriori algorithm is known to face memory constraints when dealing with large-scale datasets. To overcome this limitation, the researchers developed a parallel Apriori implementation on Spark, incorporating two key optimizations: the utilization of Spark's Broadcast Variables and the application of the Apriori Principle. By leveraging Spark's distributed computing capabilities and the inherent properties of the Apriori algorithm, the optimized implementation was able to successfully process large datasets without being hindered by the memory constraints of the traditional approach. The study conducted experiments to evaluate the performance of the optimized Apriori algorithm and compared it to a naive parallel implementation without the proposed optimizations. Furthermore, the researchers reviewed and discussed various parallel Frequent Itemset Mining algorithms beyond the Apriori algorithm.

