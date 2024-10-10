<template> 
  <view class="container">
    <!-- 按钮容器 -->
    <view class="button-container">
      <view class="buttons">
        <button @click="navigateToFindFriend" class="button">
          <image src="/static/icons/friend.png" class="button-icon" />
          <text class="button-text">查找伙伴</text>
        </button>
        <button @click="navigateToPublishProject" class="button">
          <image src="/static/icons/publish_project.png" class="button-icon" />
          <text class="button-text">发布项目</text>
        </button>
      </view>
    </view>

    <!-- 项目展示区 -->
    <swiper class="project-swiper" indicator-dots="true" autoplay="true" indicator-color="rgba(255,255,255,0.5)" indicator-active-color="#ffffff">
      <swiper-item v-for="(project, index) in projects" :key="index">
        <view class="project-item">
          <view class="project-card">
            <!-- 项目图片 -->
            <image :src="project.image" class="project-image" :alt="project.project_name"></image>
            
            <!-- 项目名字 -->
            <view class="project-name">
              <text class="project-title">{{ project.project_name }}</text>
            </view>
            
            <!-- 项目编号与查看按钮 -->
            <view class="project-field project-id-field">
              <text class="project-label">项目编号:</text>
              <view class="project-id-row">
                <text class="project-value">{{ project.project_id }}</text>
                <view class="view-button" @click="navigateToLook(project.project_id)">
                  <image src="/static/icons/look.png" class="view-icon"></image>
                  <text class="view-text">查看</text>
                </view>
              </view>
            </view>

            <view class="divider"></view>
            
            <!-- 其他项目字段 -->
            <view class="project-field">
              <text class="project-label">项目状态:</text>
              <text class="project-value">{{ project.status }}</text>
            </view>
            <view class="divider"></view>
            <view class="project-field">
              <text class="project-label">项目领域:</text>
              <text class="project-value">{{ project.field }}</text>
            </view>
            <view class="divider"></view>
            <view class="project-field">
              <text class="project-label">创建日期:</text>
              <text class="project-value">{{ project.created_at }}</text>
            </view>
          </view>
        </view>
      </swiper-item>
    </swiper>
  </view>
</template>


<script>
export default {
  data() {
    return {
      projects: [] // 初始化为空数组，等待后端数据填充
    };
  },
  methods: {
    // 获取项目信息
    fetchProjects() {
      const token = uni.getStorageSync('authToken'); // 获取保存的token
      uni.request({
        url: 'https://734dw56037em.vicp.fun/projects/projects/', // 替换为你的后端项目API
        method: 'GET',
        header: {
          'Authorization': `Token ${token}`, // 传递 token
        },
        success: (res) => {
          // console.log('请求结果:', res);
		  if (res.statusCode === 200) {
            // 成功获取项目数据，保存到 projects
            this.projects = res.data.map(project => {
				  // 格式化 created_at 日期
                  const createdAt = new Date(project.created_at);
                  project.created_at = createdAt.toISOString().split('T')[0]; // 提取日期部分
                  return project;
                });
			// console.log(JSON.stringify(this.projects))
          } else {
            // 处理错误情况
            uni.showToast({
              title: '获取项目失败',
              icon: 'none',
            });
          }
        },
        fail: (err) => {
          // 请求失败处理
          uni.showToast({
            title: '请求失败，请稍后再试',
            icon: 'none',
          });
          console.error(err);
        }
      });
    },
    // 页面跳转逻辑
    navigateToFindFriend() {
      uni.navigateTo({
        url: '/pages/home/find_friend'
      });
    },
    navigateToLook(projectId) {
      uni.navigateTo({
        url: `/pages/home/look?id=${projectId}`
      });
    },
    navigateToPublishProject() {
      uni.navigateTo({
        url: '/pages/home/publish_project'
      });
    }
  },
  // 生命周期函数，在页面加载时获取项目信息
  onLoad() {
    console.log('页面加载，开始获取项目信息'); 
	this.fetchProjects(); // 调用获取项目的方法
  }
};
</script>


<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #e0f0f1; /* 保持原背景颜色 */
  min-height: 100vh;
  overflow: hidden; /* 防止页面整体滚动 */
  animation: fadeIn 1s ease-in-out; /* 页面加载淡入效果 */
}

.button-container {
  width: 90%;
  max-width: 800rpx;
  background-color: rgba(255, 255, 255, 0.8); /* 半透明白色背景，保持内容清晰 */
  border-radius: 20rpx;
  box-shadow: 0 4rpx 8rpx rgba(0, 0, 0, 0.2);
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 20rpx 0;
  padding: 20rpx;
  
  /* 调整后的渐变背景，与整体背景 rgba(91, 174, 183, 0.05) 搭配 */
  background: linear-gradient(135deg, rgba(91, 174, 183, 0.2) 0%, rgba(91, 174, 183, 0.4) 100%);
  
  transition: transform 0.5s, background 0.5s;
}

.button-container:hover {
  
  /* 增加渐变动画，使背景颜色动态变化 */
  background: linear-gradient(135deg, rgba(91, 174, 183, 0.3) 0%, rgba(91, 174, 183, 0.5) 100%);
}


.buttons {
  display: flex;
  justify-content: space-between;
  width: 100%;
  gap: 20rpx;
}

.button {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 45%;
  background-color: rgba(255, 255, 255, 0.8); /* 半透明背景 */
  color: #009999;
  text-align: center;
  border-radius: 20rpx;
  position: relative;
  transition: transform 0.3s, box-shadow 0.3s;
  cursor: pointer;
}

.button:active {
  transform: scale(0.95); /* 点击时缩小 */
}

.button-icon {
  height: 100rpx;
  width: 100rpx;
  margin-bottom: 10rpx;
  transition: transform 0.3s;
}

.button:hover .button-icon {
  transform: rotate(20deg); /* 悬停时旋转图标 */
}

.button-text {
  font-size: 28rpx;
  font-weight: bold;
  color: #007aff;
  transition: color 0.3s;
}

.button:hover .button-text {
  color: #ff4081; /* 悬停时文字颜色变化 */
}

/* 项目展示区 */
.project-swiper {
  width: 90%;
  max-width: 1200rpx;
  height: 600px;
  margin: 0 auto;
  border-radius: 20rpx;
  overflow: hidden;
  box-shadow: 0 4rpx 16rpx rgba(0, 0, 0, 0.2);
  animation: slideIn 1s ease-in-out;
}

.swiper-item {
  display: flex;
  justify-content: center;
  align-items: center;
}

.project-item {
  display: flex;
  justify-content: center;
  align-items: flex-start; /* 内容从顶部开始 */
  background-color: #ffffff;
  padding: 20rpx;
  border-radius: 20rpx;
  box-shadow: 0 4rpx 8rpx rgba(0, 0, 0, 0.2);
  overflow: hidden; /* 防止内容溢出 */
  height: 100%; /* 确保项目项填满 Swiper */
  transition: transform 0.5s;
}

.project-item:hover {
  transform: scale(1.02); /* 悬停时轻微放大 */
}

.project-card {
  background-color: #ffffff;
  border-radius: 15px;
  box-shadow: 0 2rpx 8rpx rgba(0, 0, 0, 0.1);
  
  /* 使用百分比宽度，并设置最大宽度 */
  width: 100%;
  max-width: 300px; /* 保持项目卡片的宽度 */
  
  overflow: hidden;
  transition: transform 0.6s;
  transform-style: preserve-3d;
}

.project-card:hover {
  transform: rotateY(10deg); /* 悬停时轻微3D旋转 */
}

.project-image {
  width: 100%;
  height: 180px; /* 保持图片高度 */
  object-fit: cover;
  transition: transform 0.5s;
}

.project-card:hover .project-image {
  transform: scale(1.1); /* 图片放大效果 */
}

.project-name {
  padding: 15rpx;
  text-align: center;
}

.project-title {
  font-size: 32rpx; /* 保持字号 */
  font-weight: bold; /* 加粗 */
  color: #000000; /* 更深的颜色，增加对比度 */
  margin-bottom: 10rpx; /* 增加下方间距，提升视觉效果 */
}

.project-field {
  display: flex;
  flex-direction: column; /* 使标签和内容垂直排列 */
  margin-bottom: 20rpx; /* 增加间距 */
}

.divider {
  width: 100%;
  height: 1rpx;
  background-color: #d3d3d3;
  margin: 10rpx 0;
}

.project-label {
  font-size: 28rpx;
  font-weight: bold;
  color: #555555;
  margin-bottom: 5rpx;
}

.project-value {
  font-size: 26rpx;
  color: #333333;
  margin-top: 5rpx;
}

.project-id-row {
  display: flex;
  align-items: center;
  margin-top: 5rpx;
}

.view-button {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-left: 20rpx;
  cursor: pointer;
  transition: color 0.3s;
}

.view-button:hover {
  color: #ff4081; /* 悬停时颜色变化 */
}

.view-icon {
  width: 24rpx;
  height: 24rpx;
  margin-right: 5rpx;
  transition: transform 0.3s;
}

.view-button:hover .view-icon {
  transform: translateX(5rpx); /* 悬停时图标轻微移动 */
}

.view-text {
  font-size: 26rpx;
  color: #007aff;
  transition: color 0.3s;
}

.view-button:hover .view-text {
  color: #ff4081; /* 悬停时文字颜色变化 */
}

/* 按钮样式 */
.more-button {
  width: 100%;
  background-color: #ff3b30;
  color: #ffffff;
  text-align: center;
  padding: 10rpx;
  font-size: 16rpx;
  border: none;
  border-top: 1rpx solid #e0e0e0;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.3s;
}

.more-button:hover {
  background-color: #e60023;
  transform: translateY(-2rpx); /* 悬停时轻微上移 */
}

/* 成功提示弹窗样式（如果有的话） */
.success-popup {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #ffffff;
  border-radius: 20px;
  padding: 40rpx 30rpx;
  box-shadow: 0 4rpx 16rpx rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  align-items: center;
  z-index: 1000;
  animation: popIn 0.5s ease-out;
}

.success-icon {
  width: 80rpx;
  height: 80rpx;
  margin-bottom: 20rpx;
  animation: bounce 1s infinite;
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
  transform: scale(1.02);
}

/* 响应式设计 */
@media (max-width: 600rpx) {
  .container {
    padding: 20rpx;
  }

  .button-container {
    width: 100%;
    padding: 10rpx;
  }

  .buttons {
    flex-direction: column;
    gap: 10rpx;
  }

  .button {
    width: 100%;
  }

  .button-icon {
    height: 80rpx;
    width: 80rpx;
  }

  .button-text {
    font-size: 24rpx;
  }

  .project-swiper {
    width: 100%;
    max-width: none;
  }

  .project-item {
    padding: 10rpx;
  }

  .project-image {
    height: 140px; /* 略微减小以适应小屏设备 */
  }

  .project-title {
    font-size: 22rpx;
  }

  .project-label {
    font-size: 24rpx;
  }

  .project-value {
    font-size: 24rpx;
  }

  .view-text {
    font-size: 24rpx;
  }

  .more-button {
    font-size: 14rpx;
    padding: 8rpx;
  }

  .success-text {
    font-size: 26rpx;
  }
}

/* 动画关键帧 */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes slideIn {
  from { transform: translateY(20px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

@keyframes popIn {
  from { transform: translate(-50%, -50%) scale(0.5); opacity: 0; }
  to { transform: translate(-50%, -50%) scale(1); opacity: 1; }
}

@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10rpx); }
}
</style>
