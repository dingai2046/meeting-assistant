#!/bin/bash

# 每10分钟自动汇报进度给老板

LOG_FILE="$HOME/meeting-assistant/progress.log"
REPORT_FILE="$HOME/meeting-assistant/progress_report.md"

while true; do
    sleep 600  # 10分钟
    
    # 生成进度报告
    cat > "$REPORT_FILE" << EOF
# 开发进度报告

生成时间: $(date '+%Y-%m-%d %H:%M:%S')

## 已完成的工作

$(cat "$LOG_FILE")

## 项目文件统计

$(find ~/meeting-assistant -type f | wc -l) 个文件已创建

## 下一步计划

- 继续完善功能
- 测试和优化
- 准备演示

EOF

    echo "$(date '+%Y-%m-%d %H:%M:%S'): 进度报告已更新" >> "$LOG_FILE"
done
