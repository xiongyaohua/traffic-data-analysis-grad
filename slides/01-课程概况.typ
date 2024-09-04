#import "@preview/diatypst:0.1.0": *

#set text(font: ("Linux Libertine", "Source Han Serif"))
#show math.equation: set text(font: ("New Computer Modern Math", "KaiTi"))

#show heading.where(level: 2): set heading(outlined: false)
#show heading.where(level: 3): set heading(outlined: false)
#show heading.where(level: 4): set heading(outlined: false)

#show: slides.with(
  title: "交通数据分析", // Required
  subtitle: "贝叶斯公式及其应用",
  date: "2024.09.04",
  authors: ("熊耀华"),
  footer: false,
  layout: "small",
)

#let centered(body) = align(center, body)
#let righted(body) = align(right, body)
#let horizoned(body) = align(horizon, body)
#let important(body) = text(fill: red, body)

#outline()

= 数据分析概况

== 什么是数据分析
#horizoned[
  - 通过数据发现现实世界的规律，进而预测、控制现实世界。
    - 相关性：预测
    - 因果性：控制

  - 难点在于：
    - 复杂性
    - 不确定性

  - 一般步骤：
    - 采集数据
    - 建模
    - 解读
]


== 推荐书籍
#horizoned[
  - Strang, Gilbert. Computational science and engineering. Wellesley-Cambridge Press, 2007.
    - 微分方程建模及求解，处理确定性数据
  - McElreath, Richard. Statistical rethinking: A Bayesian course with examples in R and Stan. Chapman and Hall/CRC, 2018.
    - 统计建模求解，处理高度不确定的数据
]

= 贝叶斯概率

== 贝叶斯公式
#horizoned[
  $ Pr(H|D)=(Pr(H) dot Pr(D|H))/P(H|D) $
  #centered[或者]
  $ Pr(H|D)=Pr(H) prop Pr(D|H) $
]

读作：*后验概率*正比与*先验概率*乘以*似然概率*

#important(righted[处理不确定性的理论基础])

== 示例1
#horizoned[
  已知一个陶罐中有 $N=4$ 个球，分红黑两色。红色球个数未知。

  假设将陶罐充分晃动后盲取一个球，记录颜色，然后放回罐中。重复以上过程5次，记录如下 $D=[红,红,黑,红,黑]$。

  请估算陶罐中红球的数量。
]
#v(1cm)
两种思路：
- 修正
- 排除

== 示例2
#horizoned[
  经典硬币问题，抛硬币5次，结果 $D=[正,反,正,正,反]$。

  请估算硬币抛出正面的概率 $p$。
]
#v(1cm)
两种思路：
- 离散
- 连续

== 示例3
#horizoned[
  已知某汽车在平直道路上以10m/s匀速前行，通过某种检测器可以测量车辆的位置，表示为车辆道路起点的距离，测量结果如下：
  #centered(table(
    columns: 6,
    [测量时间s], [1], [2], [3], [4], [5],
    [距离m], [3.4], [4.7], [6.5], [7.2], [8.1],
  ))
  已知检测器存在测量误差，误差为正态分布，标准差$sigma=2$。估计车辆的实际轨迹。
]

= 采样理论

== 分布和样本

