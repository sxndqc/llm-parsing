order = """
You are a linguistic annotator. You need to follow the examples to parse a sentence into Uniform Meaning Representation step by step. You must name each variable starting with "s", followed by the number of sentence. All the tokens should only be from the sentence, and you must not hallucinate about any tokens. You should identify the main verb as the head of the tree, and analyze the clauses recursively.
"""

exemplar_dialog = [{"role":"user", "content": "Parse sentence 1 quoted in the triple backticks: ```《 世界 新闻 周报 》 是 一份 已经 停止 发行 的 美国 超市 小报 ， 以 报导 奇闻 轶事 、 都 会 传奇 、 恶搞 新闻 而 闻名 。 ```"},
                   {"role":"assistant", "content": """
                    世界新闻周报 identity 小报;
                    # sentence level graph:
(s1i2 / identity-91
  :ARG1 (s1n / newspaper
          :name (s1n2 / name
                  :op1 "《"
                  :op2 "世界"
                  :op3 "新闻"
                  :op4 "周报"
                  :op5 "》"))
  :ARG2 (s1x / 小报
          :mod (s1x2 / 超市)
          :place (s1c / country
                   :name (s1n3 / name
                           :op1 "美国"))
          :ARG1-of (s1x3 / 发行-01
                     :ARG1-of (s1x4 / 停止-01
                                :mod (s1x6 / 已经)
                                :aspect state)
                     :aspect habitual)
          :quant 1
          :unit (s1x5 / 份)
          :ARG1-of (s1x7 / 闻名-01
                     :reason (s1x8 / 报导-01
                               :ARG0 s1x
                               :ARG1 (s1a / and
                                       :op1 (s1a2 / and
                                              :op1 (s1x9 / 奇闻)
                                              :op2 (s1x10 / 轶事))
                                       :op2 (s1x11 / 传奇
                                              :mod (s1x13 / 都会))
                                       :op3 (s1x12 / 新闻
                                              :mod (s1x14 / 恶搞)))
                               :aspect habitual)
                     :aspect state))
  :aspect state)"""},
                   {"role":"user", "content": "Parse sentence 2 quoted in the triple backticks: ```该 周报 综合 了 各式各样 奇怪 的 新闻 与 专栏 ， 其中 许多 内容 都 未经 一般 的 新闻 查证 程序 。 ```"},
                   {"role":"assistant", "content": """
                    存在一个逗号，所以是"and".
                    # sentence level graph:
(s2a / and
  :op1 (s2x / 综合-01
         :ARG0 (s2x2 / 周报
                 :mod (s2x3 / 该))
         :ARG1 (s2a2 / and
                 :op1 (s2x4 / 新闻
                        :mod (s2x6 / 各式各样)
                        :mod (s2x7 / 奇怪))
                 :op2 (s2x5 / 专栏
                        :mod s2x6
                        :mod s2x7))
         :aspect habitual)
  :op2 (s2x8 / 经-01
         :ARG0 (s2x9 / 内容
                 :quant (s2x10 / 许多)
                 :mod (s2x11 / 其中))
         :ARG1 (s2x12 / 程序
                 :ARG0-of (s2i2 / identity-91
                            :ARG1 (s2x13 / 查证-01
                                    :ARG1 (s2x14 / 新闻)
                                    :aspect process))
                 :mod (s2x15 / 一般))
         :mod (s2x16 / 都)
         :aspect process))"""},
                   {"role":"user", "content": "Parse sentence 3 quoted in the triple backticks: ```该 周报 也 曾经 短暂 的 拥有 过 一个 属 自己 的 电视 节目 。```"},
                   {"role":"assistant", "content": """
                    # sentence level graph:
(s3x / 拥有-01
  :ARG0 (s3x2 / 周报
          :mod (s3x3 / 该))
  :ARG1 (s3x4 / 节目
          :medium (s3x5 / 电视)
          :ARG0-of (s3x6 / 属-02
                     :ARG1 s3x2
                     :aspect state)
          :quant 1
          :unit (s3x7 / 个))
  :mod (s3x8 / 也)
  :temporal (s3x9 / 曾经)
  :duration (s3x10 / 短暂)
  :aspect state)
                    """},
                   {"role":"user", "content": "Parse sentence 4 quoted in the triple backticks: ```目前 《 世界 新闻 周报 》 的 纸本 已经 停刊 ， 不过 仍 继续 发行 网络版 。 ```"},
                   {"role":"assistant", "content": """
# sentence level graph:
(s4b / but-91
  :ARG1 (s4x / 停刊-01
          :ARG0 (s4x5 / 纸本
                  :part-of (s4n / newspaper
                             :name (s4n2 / name
                                     :op1 "《"
                                     :op2 "世界"
                                     :op3 "新闻"
                                     :op4 "周报"
                                     :op5 "》")))
          :temporal (s4x3 / 目前)
          :mod (s4x4 / 已经)
          :aspect performance)
  :ARG2 (s4x2 / 继续-01
          :ARG1 (s4x6 / 发行-01
                  :ARG1 (s4x7 / 网络版)
                  :aspect habitual)
          :mod (s4x8 / 仍)
          :aspect activity))"""},
                   {"role":"user", "content": "Parse sentence 5 quoted in the triple backticks: ```由于 其 荒诞不经 的 内容 ， 该 周报 被 称为 美国 历史 上 最富 创意 的 报纸 。 ```"},
                   {"role":"assistant", "content":"""
# sentence level graph:
(s5x / 称为-01
  :ARG1 (s5x2 / 周报
          :mod (s5x3 / 该))
  :ARG2 (s5x4 / 报纸
          :ARG1-of (s5h / have-degree-91
                     :ARG2 (s5x5 / 富-01
                             :ARG1 (s5x6 / 创意)
                             :aspect state)
                     :ARG3 (s5x7 / 最))
          :temporal (s5x8 / 上
                      :op1 (s5x9 / 历史
                             :place (s5c / country
                                      :name (s5n / name
                                              :op1 "美国")))))
  :reason (s5x10 / 内容
            :poss s5x2
            :mod (s5x11 / 荒诞不经))
  :aspect performance)"""},
                   {"role":"user", "content": "Parse sentence 6 quoted in the triple backticks: ```《 世界 新闻 周报 》 创刊 于 1979 年 。 ```"},
                   {"role":"assistant", "content": """
# sentence level graph:
(s6x / 创刊-01
  :ARG0 (s6n / newspaper
          :name (s6n2 / name
                  :op1 "《"
                  :op2 "世界"
                  :op3 "新闻"
                  :op4 "周报"
                  :op5 "》"))
  :temporal (s6d / date-entity
              :year 1979)
  :aspect performance)"""},
                   {"role":"user", "content": "Parse sentence 7 quoted in the triple backticks: ```创始人 格内洛索 · 波普 因为 旗下 的 八卦 小报 《 国家 询问 报 》 将 由 黑白 版面 改为 彩色 版面 ， 为 充分 运用 遗留 下来 的 黑白 印刷机 ， 于是 创立 了 黑白 版面 的 《 世界 新闻 周报 》 ， 容纳 那些 不 符合 《 国家 询问 报 》 标准 的 文章 。 ```"},
                   {"role":"assistant", "content": """
# sentence level graph:
(s7h / have-reason-91
  :ARG1 (s7h2 / have-purpose-91
          :ARG1 (s7x13 / 创立-01
                  :ARG0 (s7i3 / individual-person
                          :name (s7n5 / name
                                  :op1 "格内洛索"
                                  :op2 "·"
                                  :op3 "波普")
                          :ARG1-of (s7h3 / have-org-role-91
                                     :ARG3 (s7x22 / 人
                                             :ARG0-of (s7x23 / 创始-00
                                                        :aspect performance))))
                  :ARG1 (s7x14 / 版面
                          :mod (s7x15 / 黑白)
                          :part-of (s7n3 / newspaper
                                     :name (s7n4 / name
                                             :op1 "《"
                                             :op2 "世界"
                                             :op3 "新闻"
                                             :op4 "周报"
                                             :op5 "》"))
                          :ARG0-of (s7x17 / 容纳-01
                                     :ARG1 (s7x18 / 文章
                                             :mod (s7x19 / 那些)
                                             :ARG0-of (s7x20 / 符合-01
                                                        :ARG1 (s7x21 / 标准
                                                                :poss s7n)
                                                        :aspect state
                                                        :polarity -))
                                     :aspect process))
                  :aspect performance)
          :ARG2 (s7x8 / 运用-01
                  :ARG1 (s7x10 / 印刷机
                          :mod (s7x11 / 黑白)
                          :ARG1-of (s7x12 / 遗留-01
                                     :aspect performance))
                  :manner (s7x9 / 充分)
                  :aspect activity)
          :aspect state)
  :ARG2 (s7x / 改为-01
          :ARG1 (s7x4 / 版面
                  :part-of (s7n / newspaper
                             :name (s7n2 / name
                                     :op1 "《"
                                     :op2 "国家"
                                     :op3 "询问"
                                     :op4 "报"
                                     :op5 "》")
                             :ARG1-of (s7i2 / identity-91
                                        :ARG2 (s7x5 / 小报
                                                :mod (s7x6 / 旗下)
                                                :mod (s7x7 / 八卦))))
                  :mod (s7x16 / 黑白))
          :ARG2 (s7x2 / 版面
                  :mod (s7x3 / 彩色))
          :aspect performance)
  :aspect state)"""},
                   {"role":"user", "content": "Parse sentence 8 quoted in the triple backticks: ```黑白 印刷 也 成 了 该刊 的 特色 。 ```"},
                   {"role":"assistant", "content": """# sentence level graph:
(s8x / 成-01
  :ARG0 (s8x2 / 印刷-01
          :manner (s8x3 / 黑白)
          :aspect habitual)
  :ARG1 (s8x4 / 特色
          :poss (s8x5 / 刊
                  :mod (s8x6 / 该)))
  :mod (s8x7 / 也)
  :aspect performance)
"""},
                   {"role":"user", "content": "Parse sentence 9 quoted in the triple backticks: ```在 1980 年代 ， 《 世界 新闻 周报 》 发行量 达到 120 万 份 。 ```"},
                   {"role":"assistant", "content": """
# sentence level graph:
(s9x / 达到-01
  :ARG0 (s9x2 / 量
          :quant-of (s9x3 / 发行-01
                      :ARG1 (s9n / newspaper
                              :name (s9n2 / name
                                      :op1 "《"
                                      :op2 "世界"
                                      :op3 "新闻"
                                      :op4 "周报"
                                      :op5 "》")))
          :ARG1-of (s9h / have-quant-91
                     :ARG2 1200000
                     :unit (s9x4 / 份)))
  :temporal (s9d / date-entity
              :era 1980)
  :aspect performance)
"""},
                   {"role":"user", "content": "Parse sentence 10 quoted in the triple backticks: ```不过 至 2007 年 ， 该刊 发行量 已经 跌至 8 万 3 千份 。 ```"},
                   {"role":"assistant", "content": """
# sentence level graph:
(s10x / 跌-01
  :ARG0 (s10x2 / 量
          :quant-of (s10x3 / 发行-01
                      :ARG1 (s10x4 / 刊
                              :mod (s10x5 / 该)))
          :ARG1-of (s10h / have-quant-91
                     :ARG2 83000
                     :unit (s10x7 / 份)))
  :temporal (s10d / date-entity
              :year 2007)
  :mod (s10x6 / 已经)
  :aspect performance)"""}]