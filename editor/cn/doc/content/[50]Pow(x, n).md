<p>实现&nbsp;<a href="https://www.cplusplus.com/reference/valarray/pow/" target="_blank">pow(<em>x</em>, <em>n</em>)</a>&nbsp;，即计算 <code>x</code> 的整数&nbsp;<code>n</code> 次幂函数（即，<code>x<sup>n</sup></code><sup><span style="font-size:10.8333px"> </span></sup>）。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>x = 2.00000, n = 10
<strong>输出：</strong>1024.00000
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>x = 2.10000, n = 3
<strong>输出：</strong>9.26100
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>x = 2.00000, n = -2
<strong>输出：</strong>0.25000
<strong>解释：</strong>2<sup>-2</sup> = 1/2<sup>2</sup> = 1/4 = 0.25
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li><code>-100.0 &lt; x &lt; 100.0</code></li> 
 <li><code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup>-1</code></li> 
 <li><code>n</code>&nbsp;是一个整数</li> 
 <li>要么 <code>x</code> 不为零，要么 <code>n &gt; 0</code> 。</li> 
 <li><code>-10<sup>4</sup> &lt;= x<sup>n</sup> &lt;= 10<sup>4</sup></code></li> 
</ul>

<details><summary><strong>Related Topics</strong></summary>递归 | 数学</details><br>

<div>👍 1332, 👎 0<span style='float: right;'><span style='color: gray;'><a href='https://github.com/labuladong/fucking-algorithm/discussions/939' target='_blank' style='color: lightgray;text-decoration: underline;'>bug 反馈</a> | <a href='https://labuladong.gitee.io/article/fname.html?fname=jb插件简介' target='_blank' style='color: lightgray;text-decoration: underline;'>使用指南</a> | <a href='https://labuladong.online/algo/images/others/%E5%85%A8%E5%AE%B6%E6%A1%B6.jpg' target='_blank' style='color: lightgray;text-decoration: underline;'>更多配套插件</a></span></span></div>

<div id="labuladong"><hr>

**通知：算法可视化编辑器上线，[点击体验](https://labuladong.online/algo/intro/visualize/)！**

<details><summary><strong>labuladong 思路</strong></summary>

## 基本思路

幂运算是经典的数学运算技巧了，建议你看下前文 [如何高效进行模幂运算](https://labuladong.github.io/article/fname.html?fname=superPower) 就能很容易理解解法代码里的思想了。这道题唯一有点恶心的就是 `k` 的取值范围特别大，不能直接加符号，否则会造成整型溢出，具体解法看代码吧。

**标签：[数学](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAxODQxMDM0Mw==&action=getalbum&album_id=2122023604245659649)**

## 解法代码

提示：🟢 标记的是我写的解法代码，🤖 标记的是 chatGPT 翻译的多语言解法代码。如有错误，可以 [点这里](https://github.com/labuladong/fucking-algorithm/issues/1113) 反馈和修正。

<div class="tab-panel"><div class="tab-nav">
<button data-tab-item="cpp" class="tab-nav-button btn " data-tab-group="default" onclick="switchTab(this)">cpp🤖</button>

<button data-tab-item="python" class="tab-nav-button btn " data-tab-group="default" onclick="switchTab(this)">python🤖</button>

<button data-tab-item="java" class="tab-nav-button btn active" data-tab-group="default" onclick="switchTab(this)">java🟢</button>

<button data-tab-item="go" class="tab-nav-button btn " data-tab-group="default" onclick="switchTab(this)">go🤖</button>

<button data-tab-item="javascript" class="tab-nav-button btn " data-tab-group="default" onclick="switchTab(this)">javascript🤖</button>
</div><div class="tab-content">
<div data-tab-item="cpp" class="tab-item " data-tab-group="default"><div class="highlight">

```cpp
// 注意：cpp 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
// 本代码已经通过力扣的测试用例，应该可直接成功提交。

class Solution {
public:
    double myPow(double a, int k) {
        if (k == 0) return 1;

        if (k == INT_MIN) {
            // 把 k 是 INT_MIN 的情况单独拿出来处理
            // 避免 -k 整型溢出
            return myPow(1 / a, -(k + 1)) / a;
        }

        if (k < 0) {
            return myPow(1 / a, -k);
        }

        if (k % 2 == 1) {
            // k 是奇数
            return (a * myPow(a, k - 1));
        } else {
            // k 是偶数
            double sub = myPow(a, k / 2);
            return (sub * sub);
        }
    }
};
```

</div></div>

<div data-tab-item="python" class="tab-item " data-tab-group="default"><div class="highlight">

```python
# 注意：python 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
# 本代码已经通过力扣的测试用例，应该可直接成功提交。

class Solution:
    def myPow(self, a: float, k: int) -> float:
        if k == 0:
            return 1

        if k == -2147483648:
            # 把 k 是 INT_MIN 的情况单独拿出来处理
            # 避免 -k 整型溢出
            return self.myPow(1 / a, -(k + 1)) / a

        if k < 0:
            return self.myPow(1 / a, -k)

        if k % 2 == 1:
            # k 是奇数
            return a * self.myPow(a, k - 1)
        else:
            # k 是偶数
            sub = self.myPow(a, k // 2)
            return sub * sub
```

</div></div>

<div data-tab-item="java" class="tab-item active" data-tab-group="default"><div class="highlight">

```java
class Solution {
    public double myPow(double a, int k) {
        if (k == 0) return 1;

        if (k == Integer.MIN_VALUE) {
            // 把 k 是 INT_MIN 的情况单独拿出来处理
            // 避免 -k 整型溢出
            return myPow(1 / a, -(k + 1)) / a;
        }

        if (k < 0) {
            return myPow(1 / a, -k);
        }

        if (k % 2 == 1) {
            // k 是奇数
            return (a * myPow(a, k - 1));
        } else {
            // k 是偶数
            double sub = myPow(a, k / 2);
            return (sub * sub);
        }
    }
}
```

</div></div>

<div data-tab-item="go" class="tab-item " data-tab-group="default"><div class="highlight">

```go
// 注意：go 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
// 本代码已经通过力扣的测试用例，应该可直接成功提交。

// Golang Code
func myPow(a float64, k int) float64 {
    if k == 0 {
        return 1
    }

    if k == math.MinInt32 {
        // 把 k 是 INT_MIN 的情况单独拿出来处理
        // 避免 -k 整型溢出
        return myPow(1 / a, -(k + 1)) / a
    }

    if k < 0 {
        return myPow(1 / a, -k)
    }
    if k % 2 == 1 {
        // k 是奇数
        return (a * myPow(a, k - 1))
    } else {
        // k 是偶数
        sub := myPow(a, k / 2)
        return (sub * sub)
    }
}
```

</div></div>

<div data-tab-item="javascript" class="tab-item " data-tab-group="default"><div class="highlight">

```javascript
// 注意：javascript 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
// 本代码已经通过力扣的测试用例，应该可直接成功提交。

/**
 * @param {number} a
 * @param {number} k
 * @return {number}
 */
var myPow = function(a, k) {
    if (k === 0) return 1;

    if (k === -2147483648) {
        // 把 k 是 INT_MIN 的情况单独拿出来处理
        // 避免 -k 整型溢出
        return myPow(1 / a, -(k + 1)) / a;
    }

    if (k < 0) {
        return myPow(1 / a, -k);
    }

    if (k % 2 === 1) {
        // k 是奇数
        return (a * myPow(a, k - 1));
    } else {
        // k 是偶数
        const sub = myPow(a, k / 2);
        return (sub * sub);
    }
};
```

</div></div>
</div></div>

<hr /><details open hint-container details><summary style="font-size: medium"><strong>🌈🌈 算法可视化 🌈🌈</strong></summary><div id="data_powx-n" data="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"></div><div class="resizable aspect-ratio-container" style="height: 100%;">
<div id="iframe_powx-n"></div></div>
</details><hr /><br />

**类似题目**：
  - [剑指 Offer 16. 数值的整数次方 🟠](/problems/shu-zhi-de-zheng-shu-ci-fang-lcof)

</details>
</div>

