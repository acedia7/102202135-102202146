<template>
  <view class="container">
    <!-- 顶部宣传图与搜索框 -->
    <view class="header">
      <image class="header-image" src="/static/photo/join_us.jpg"></image>
      <view class="search-bar">
        <input
          type="text"
          placeholder="请输入搜索内容"
          v-model="searchQuery"
          class="search-input"
          @input="filterProjects"
        />
        <button @click="search" class="search-button">
          <image src="/static/icons/search.png" class="search-icon"></image>
        </button>
      </view>
    </view>

    <!-- 项目展示区 -->
    <scroll-view class="projects-section" scroll-y>
      <view class="projects-container">
        <view
          class="project-card"
          v-for="(project, index) in filteredProjects"
          :key="index"
          @click="viewProject(project)"
          :style="{ animationDelay: `${index * 0.1}s` }"
        >
          <image :src="project.image" class="project-image"></image>
          <view class="project-title">{{ project.title }}</view>
          <button class="more-button">了解更多</button>
        </view>
      </view>
    </scroll-view>

    <!-- 成功提示弹窗 -->
    <view v-if="showSuccess" class="success-popup">
      <image src="/static/icons/success.png" class="success-icon"></image>
      <view class="success-text">操作成功！</view>
      <button class="close-button" @click="closePopup">关闭</button>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: '', // 搜索框输入内容
      projects: [
        {
          title: '通过深度学习识别云朵形状与天气气候的关联',
          image: '/static/photo/project1.jpg',
        },
        {
          title: '牙齿从中间折还是从底部折对家庭和谐的影响',
          image: '/static/photo/project2.jpg',
        },
        {
          title: '牛顿苹果树下Wi-Fi信号强度的历史演变研究',
          image: '/static/photo/project3.jpg',
        },
        {
          title: '开发一种检测冰淇淋融化速度的智能手机应用',
          image: '/static/photo/project4.jpg',
        },
      ],
      filteredProjects: [], // 过滤后的项目列表
      showSuccess: false, // 控制成功弹窗显示
    };
  },
  created() {
    // 初始化显示所有项目
    this.filteredProjects = this.projects;
  },
  methods: {
    // 实时搜索功能
    filterProjects() {
      if (this.searchQuery.trim() === '') {
        this.filteredProjects = this.projects;
      } else {
        const query = this.searchQuery.toLowerCase();
        this.filteredProjects = this.projects.filter((project) =>
          project.title.toLowerCase().includes(query)
        );
      }
    },
    // 搜索按钮点击事件
    search() {
      this.filterProjects();
      this.showSuccessPopup('搜索完成！');
    },
    // 查看项目详情
    viewProject(project) {
      this.showSuccessPopup(`查看项目：${project.title}`);
      // 跳转到项目详情页面
      uni.navigateTo({
        url: `/pages/find_project/know_more?title=${encodeURIComponent(project.title)}`,
      });
    },
    // 显示成功弹窗
    showSuccessPopup(message) {
      this.showSuccess = true;
      uni.showToast({
        title: message,
        icon: 'none',
        duration: 2000,
      });
    },
    // 关闭弹窗
    closePopup() {
      this.showSuccess = false;
    },
  },
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  background-color: #f0f4f8; /* 保持原有背景色 */
  min-height: 100vh;
  overflow: hidden;
}

/* 顶部宣传图与搜索框 */
.header {
  position: fixed; /* 固定定位 */
  top: 0; /* 固定在页面顶部 */
  left: 0;
  width: 100%; /* 覆盖整个页面宽度 */
  height: 220px; /* 保持原有高度 */
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #f0f4f8; /* 保持原有背景色 */
  z-index: 1000; /* 确保在最前面 */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* 添加轻微阴影 */
}

.header-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s;
}

.header-image:hover {
  transform: scale(1.05);
}

.search-bar {
  position: absolute;
  bottom: -25px;
  display: flex;
  width: 80%;
  max-width: 600px; /* 设置最大宽度 */
  background-color: #ffffff;
  border-radius: 30px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
  padding: 10px 20px;
  align-items: center;
  animation: slideUp 0.5s ease forwards;
}

@keyframes slideUp {
  from {
    bottom: -60px;
    opacity: 0;
  }
  to {
    bottom: -25px;
    opacity: 1;
  }
}

/* 搜索输入框 */
.search-input {
  flex: 1;
  padding: 10px 15px;
  border: none;
  border-radius: 30px;
  outline: none;
  font-size: 16px;
  background-color: transparent;
  transition: all 0.3s ease;
}

.search-input:focus {
  transform: scale(1.05);
}

.search-button {
  background: none;
  border: none;
  padding: 5px;
  outline: none;
  margin-left: 10px;
  cursor: pointer;
  transition: transform 0.2s;
}

.search-button:hover {
  transform: scale(1.2);
}

.search-icon {
  width: 24px;
  height: 24px;
}

/* 项目展示区 */
.projects-section {
  flex: 1;
  margin-top: 220px; /* 保持顶部边距 */
  padding: 0px;
  background-color: #f0f4f8; /* 保持原有背景色 */
  display: flex;
  justify-content: center;
  align-items: flex-start;
}

.projects-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  width: 100%;
  max-width: 1200rpx;
  margin: 0 auto;
  box-sizing: border-box;
}

.project-card {
  background-color: #ffffff;
  border-radius: 15px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 300px;
  overflow: hidden;
  transition: transform 0.3s, box-shadow 0.3s;
  animation: fadeInUp 0.6s forwards;
  opacity: 0;
}

@keyframes fadeInUp {
  from {
    transform: translateY(20px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

.project-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
}

.project-image {
  width: 100%;
  height: 160px;
  object-fit: cover;
  transition: transform 0.5s;
}

.project-card:hover .project-image {
  transform: scale(1.05);
}

.project-title {
  padding: 15px;
  font-size: 24rpx;
  font-weight: bold;
  color: #333333;
  text-align: center;
}

/* 按钮样式 */
.more-button {
  width: 100%;
  background-color: #ff3b30;
  color: #ffffff;
  text-align: center;
  padding: 10px;
  font-size: 16px;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s;
}

.more-button:hover {
  background-color: #e60023;
  transform: scale(1.05);
}

/* 成功提示弹窗样式 */
.success-popup {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: rgba(0, 0, 0, 0.9);
  border-radius: 20px;
  padding: 40rpx 30rpx;
  box-shadow: 0 4rpx 16rpx rgba(0, 0, 0, 0.5);
  display: flex;
  flex-direction: column;
  align-items: center;
  z-index: 1001;
  animation: popIn 0.3s ease forwards;
}

@keyframes popIn {
  from {
    transform: translate(-50%, -50%) scale(0.8);
    opacity: 0;
  }
  to {
    transform: translate(-50%, -50%) scale(1);
    opacity: 1;
  }
}

.success-icon {
  width: 80rpx;
  height: 80rpx;
  margin-bottom: 20rpx;
}

.success-text {
  font-size: 30rpx;
  color: #28a745;
  margin-bottom: 30rpx;
}

.close-button {
  width: 120rpx;
  height: 50rpx;
  background-color: #28a745;
  color: #ffffff;
  font-size: 26rpx;
  border: none;
  border-radius: 10rpx;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s;
}

.close-button:hover {
  background-color: #1e7e34;
  transform: scale(1.05);
}

/* 响应式设计 */
@media (max-width: 600rpx) {
  .header {
    height: 180px;
  }

  .search-bar {
    width: 90%;
    bottom: -20px;
    padding: 8px 15px;
  }

  .project-title {
    font-size: 28rpx;
  }

  .more-button {
    font-size: 14px;
    padding: 8px;
  }

  .success-text {
    font-size: 26rpx;
  }
}
</style>
