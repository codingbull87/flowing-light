# Flowing Light Design System v4.0 (Aesthetic Refinement Edition)

本文件是 Flowing Light 的单一事实来源（Single Source of Truth）。
基于近期的视觉与交互重构，本版本融合了高质感的玻璃拟物（Glassmorphism）、优雅的版式层级（Playfair Display + Inter）以及高性能的滚动动效（GSAP 优化）规范。

---

## 1. 系统定位与目标

### 1.1 Creative North Star
- 关键词：**Luminescent Parchment / 数字策展 / 轻盈而有分量**
- 本质：把页面当成“阅读展陈空间”，通过高对比度字体和通透的玻璃质感，营造杂志级别的审美体验。
- 体验目标：首屏有气质，正文可沉浸，交互有反馈（极度流畅），系统可迭代。

### 1.2 适用范围
- 生产页面：`index.html`、`archive.html`、`about.html`、`episodes/vol*/index.html`
- 设计系统页面：`design-system/design-system-v3.html`
- 运行支撑：`js/tailwind-config.js`、`css/style.css`、`js/layout.js`、`js/site.js`

### 1.3 三条总原则
1. **先排版，后装饰**：文字本身即是设计（Playfair Display 与 Inter 的极致对比）。
2. **绝对流畅**：严禁在滚动动效中使用极耗性能的属性（如 blur），确保移动端 60fps。
3. **全局通透**：确保背景渐变（Ethereal Gradient）在各区块中自然透出，避免被实色背景截断。

---

## 2. 基础令牌（Foundation Tokens）

### 2.1 Color Tokens
**核心色彩**
- 强调色（Accent）：金句与高亮元素使用特制强调色（如 `#C8523A`）。
- 文本色：主标题支持柔和深色（如 `#1A1A1A` 或 `#555555` 视场景而定），保持对比度的同时避免死黑。
- 背景底色（Background）：核心区块必须使用 `bg-transparent`，让底层的 `ethereal-gradient-bg` 渐变全局透出。

### 2.2 Typography Tokens (全新字体栈)
- `font-display` / `font-headline`：**Playfair Display**（优雅、高对比度的衬线体，用于 Hero 标题、章节标题、金句引用）。
- `font-body` / `font-label`：**Inter**（清晰、现代的无衬线体，用于正文、标签、UI 按钮、元数据）。

**响应式排版缩放规则（以 About 页为例）**
- **H2 (二级标题)**：`text-2xl sm:text-3xl lg:text-4xl`（克制、不过度放大）。
- **P (正文段落)**：`text-base md:text-lg`（保证可读性）。
- **极宽行距**：金句或特殊排版区使用 `leading-[2.5]`，区块间距使用 `space-y-12 md:space-y-16`。

### 2.3 Radius / Shadow / Layer Tokens
- 玻璃面板（Glassmorphism）：核心视觉容器统一使用 `bg-white/40 backdrop-blur-[60px]`。
- 柔和阴影：优先使用极弱的白光边缘或透明度边框来区分层级，而非重阴影。

### 2.4 Motion Tokens (高性能动效优化)
- **时长（Duration）**：标准叙事入场统一收敛至 **`0.8s`**。
- **缓动（Easing）**：核心缓动曲线统一为 **`power2.out`**。
- **触发时机（ScrollTrigger）**：前置到 `top 80%`，避免移动端滚动留白过长。
- **性能红线（黑名单）**：**严禁在滚动动画中使用 CSS `blur()` 滤镜**，仅允许使用 `transform` (y 位移) 和 `opacity`。

---

## 3. 全局结构硬规则

### 3.1 导航标签系统 (Tags)
- **双语与响应式**：标签区必须使用 `flex-wrap`，防止在移动端因中英文混排导致内容溢出出画。
- **装饰元素**：竖向分隔线等装饰在移动端必须隐藏（`hidden md:block`）。

### 3.2 Footer 策略 (极窄磨砂)
- 质感：使用 `bg-white/30 backdrop-blur-md` 打造轻薄的毛玻璃尾封。
- 尺寸：大幅收窄高度，统一使用 `py-6 md:py-8`。

### 3.3 Golden Quote 金句视口
- 高度收敛：使用 `min-h-[70vh]` 替代 `h-screen`，缩短移动端无意义的滑动距离。
- 纯粹排版：去除多余的箭头和链接，专注三行文字本身的排版力量。

---

## 4. UI Kit 组件规范（更新版）

### 4.1 Hero Panel Container
- 样式：`<div class="bg-white/40 backdrop-blur-[60px] ...">`
- 要求：必须与底层的全局渐变背景产生光学反应，不可被实色遮挡。

### 4.2 响应式标签组 (Responsive Tag Group)
- 结构：`<div class="flex flex-wrap items-center gap-x-4 ...">`
- 字体：纯英文优先，或者英文配合极低透明度的中文字体，提升设计感。

### 4.3 沉浸式金句区 (Immersive Quote)
- 间距：内部行距 `leading-[2.5]`，段落间距 `space-y-12 md:space-y-16`。
- 色彩：局部文本提亮（`text-[#C8523A]`）。

---

## 5. 生产页面映射（规范落地）

### 5.1 首页 `index.html`
- 重点：重构的 Hero 玻璃面板；去除 blur 的顺滑 GSAP 滚动；精简且极具张力的 70vh 金句区。

### 5.2 关于页 `about.html`
- 重点：克制的 H2 标题字号；字字珠玑的短段落；保留透明底色以延续首页的情绪铺垫。

### 5.3 详情页 `episodes/vol*/index.html`
- 重点：共享极窄毛玻璃 Footer；正文采用 Inter 字体，保证长文阅读的绝对清晰。

---

## 6. 设计系统治理（Governance）

### 6.1 变更流程
1. 先在 `design-system-v3.html` 验证新排版和玻璃质感。
2. 确认在移动端（iPhone 尺寸）没有横向溢出。
3. 确认 GSAP 滚动在移动设备上无掉帧卡顿。

### 6.2 回归检查（Checklist）
- [ ] 是否存在任何硬编码的 `h-screen` 导致移动端滚动过长？（应使用 `min-h-[70vh]`）
- [ ] 滚动动画中是否移除了所有的 `blur` 效果？
- [ ] 多元素同行排列时，是否加上了 `flex-wrap`？
- [ ] 是否因为增加了背景色而覆盖了全局的 `ethereal-gradient-bg`？
