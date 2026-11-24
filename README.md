# pairwise-spotlight-shadow-atlas

## 领域

游戏、图形与多媒体

## 主题

聚光灯阴影图集分页

## 说明

灯 ID 稳定映射、页回收与翻转采样。

初始状态下 `graphics/spotlight_shadow_atlas.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
