<template>
  <view class="container">
    <!-- 个人信息卡 -->
    <view class="info-card animated fadeInUp">
      <image :src="user.avatar" class="avatar" />
      <view class="user-info">
        <text class="user-name">{{ user.name }}</text>
        <text class="user-school">{{ user.school }}</text>
        <view class="user-stats">
          <view class="stat-item">
            <text class="stat-number">{{ user.following }}</text>
            <text class="stat-label">关注</text>
          </view>
          <view class="stat-item">
            <text class="stat-number">{{ user.followers }}</text>
            <text class="stat-label">粉丝</text>
          </view>
        </view>
      </view>
    </view>

    <!-- 常用工具框 -->
    <view class="tools-container animated fadeInUp delay-1s">
      <view class="tools-header">
        <text class="tools-title">常用工具</text>
      </view>
      <view class="tools-card">
        <view class="tools-row">
          <view class="tool-item" @click="navigateTo('个人信息')">
            <image src="/static/icons/personal_info.png" class="tool-icon" />
            <text class="tool-name">个人信息</text>
          </view>
          <view class="tool-item" @click="navigateTo('反馈建议')">
            <image src="/static/icons/feedback.png" class="tool-icon" />
            <text class="tool-name">反馈建议</text>
          </view>
          <view class="tool-item" @click="navigateTo('账户安全')">
            <image src="/static/icons/account_security.png" class="tool-icon" />
            <text class="tool-name">账户安全</text>
          </view>
        </view>
        <view class="tools-row">
          <view class="tool-item" @click="navigateTo('系统设置')">
            <image src="/static/icons/system_settings.png" class="tool-icon" />
            <text class="tool-name">系统设置</text>
          </view>
          <view class="tool-item" @click="navigateTo('关于我们')">
            <image src="/static/icons/about_us.png" class="tool-icon" />
            <text class="tool-name">关于我们</text>
          </view>
          <!-- 捐赠按钮 -->
          <view class="tool-item donate-button" @click="navigateTo('个人捐赠')">
            <image src="/static/icons/donate.png" class="tool-icon" />
            <text class="tool-name">个人捐赠</text>
          </view>
        </view>
      </view>
    </view>
  </view>
</template>



<script>
export default {
  data() {
    return {
      // 初始化用户信息
      user: {
        name: '',
        school: '',
        avatar: '',
        following: 0,
        followers: 0
      },
      tools: [
        { name: '个人信息', icon: '/static/icons/personal_info.png', path: '/pages/person/personal_info' },
        { name: '反馈建议', icon: '/static/icons/feedback.png', path: '/pages/person/feedback' },
        { name: '账户安全', icon: '/static/icons/account_security.png', path: '/pages/person/account_security' },
        { name: '系统设置', icon: '/static/icons/system_settings.png', path: '/pages/person/system_settings' },
        { name: '关于我们', icon: '/static/icons/about_us.png', path: '/pages/person/about_us' },
        { name: '个人捐赠', icon: '/static/icons/donate.png', path: '/pages/person/donate' } // 新增捐赠按钮
      ]
    };
  },
  onLoad() {
    this.getUserProfile();
  },
  onShow() {
    this.getUserProfile(); // 重新获取用户资料
  }

  methods: {
    navigateTo(page) {
      const tool = this.tools.find(t => t.name === page);
      if (tool) {
        uni.navigateTo({
          url: tool.path
        });
      }
    },
    async getUserProfile() {
      try {
        const token = uni.getStorageSync('authToken'); // 获取存储的 token
        const response = await uni.request({
          url: 'https://734dw56037em.vicp.fun/users/get_user_profile/', // 用户信息接口
          method: 'GET',
          header: {
            'Authorization': `Token ${token}`,
            'Content-Type': 'application/json'
          }
        });
    
        // 检查状态码并处理用户信息
        if (response.statusCode === 200) {
          const userData = response.data; // 从 response.data 中提取用户数据
          this.user.name = userData.name;
          this.user.school = userData.school;
          this.user.avatar = userData.avatar;
          this.user.following = 0; // 根据需要动态更新
          this.user.followers = 0; // 根据需要动态更新
        } else {
          console.error('获取用户信息失败:', response.data);
        }
      } catch (error) {
        console.error('请求出错:', error);
      }
    }

  }
};
</script>



<style scoped>
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes backgroundGradient {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

.animated {
  animation-duration: 1s;
  animation-fill-mode: both;
}

.fadeInUp {
  animation-name: fadeInUp;
}

.delay-1s {
  animation-delay: 1s;
}

/* 背景渐变动画 */
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
/*  background: linear-gradient(-45deg, #f5f7fa, #c3cfe2, #a1c4fd, #c2e9fb); */
  background-size: 400% 400%;
  animation: backgroundGradient 15s ease infinite;
  padding: 40rpx;
  min-height: 100vh;
  box-sizing: border-box;
}

/* 个人信息卡样式 */
.info-card {
  display: flex;
  align-items: center;
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 20rpx;
  padding: 40rpx;
  box-shadow: 0 4rpx 16rpx rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 800rpx;
  margin-bottom: 40rpx;
  transition: transform 0.3s, box-shadow 0.3s;
}

.info-card:hover {
  transform: translateY(-10rpx);
  box-shadow: 0 8rpx 24rpx rgba(0, 0, 0, 0.2);
}

.avatar {
  width: 160rpx; /* 放大头像 */
  height: 160rpx; /* 放大头像 */
  border-radius: 80rpx;
  margin-right: 40rpx;
  object-fit: cover;
  border: 4rpx solid #2196f3;
  transition: transform 0.3s;
}

.avatar:hover {
  transform: scale(1.05);
}

/* 用户信息样式 */
.user-info {
  display: flex;
  flex-direction: column;
  justify-content: center;
  flex: 1;
}

.user-name {
  font-size: 40rpx;
  font-weight: bold;
  color: #333333;
  margin-bottom: 8rpx;
  text-shadow: 1rpx 1rpx 2rpx rgba(0, 0, 0, 0.1);
}

.user-school {
  font-size: 30rpx;
  color: #888888;
  margin-bottom: 20rpx;
}

/* 关注和粉丝数样式 */
.user-stats {
  display: flex;
  flex-direction: row;
  margin-top: 10rpx;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-right: 60rpx;
  transition: transform 0.3s;
}

.stat-item:hover {
  transform: scale(1.1);
}

.stat-label {
  font-size: 24rpx;
  color: #666666;
  margin-top: 5rpx;
}

.stat-number {
  font-size: 32rpx;
  color: #333333;
  font-weight: bold;
  position: relative;
}

.stat-number::after {
  content: '';
  position: absolute;
  width: 8rpx;
  height: 8rpx;
  background-color: #2196f3;
  border-radius: 50%;
  top: -10rpx;
  right: -10rpx;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% {
    transform: scale(0.8);
    opacity: 1;
  }
  100% {
    transform: scale(2.5);
    opacity: 0;
  }
}

/* 常用工具框样式 */
.tools-container {
  width: 100%;
  max-width: 800rpx;
}

.tools-header {
  width: 100%;
  padding: 20rpx 30rpx;
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 20rpx 20rpx 0 0;
  box-shadow: 0 4rpx 8rpx rgba(0, 0, 0, 0.1);
  margin-bottom: -1px; /* 连接工具卡 */
}

.tools-title {
  font-size: 32rpx;
  color: #333333;
  font-weight: bold;
  text-shadow: 1rpx 1rpx 2rpx rgba(0, 0, 0, 0.1);
}

.tools-card {
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 0 0 20rpx 20rpx;
  padding: 20rpx;
  box-shadow: 0 4rpx 12rpx rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s;
}

.tools-card:hover {
  background-color: rgba(255, 255, 255, 1);
}

.tools-row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 30rpx;
}

.tool-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 30%;
  padding: 20rpx 10rpx;
  cursor: pointer;
  transition: transform 0.3s, box-shadow 0.3s, background-color 0.3s;
  border-radius: 15rpx;
}

.tool-item:hover {
  transform: scale(1.05);
  box-shadow: 0 8rpx 24rpx rgba(0, 0, 0, 0.2);
  background-color: #f0f0f0;
}

.tool-icon {
  width: 60rpx;
  height: 60rpx;
  margin-bottom: 15rpx;
  transition: transform 0.3s;
}

.tool-item:hover .tool-icon {
  transform: rotate(10deg);
}

.tool-name {
  font-size: 28rpx;
  color: #333333;
  text-align: center;
  transition: color 0.3s;
}

.tool-item:hover .tool-name {
  color: #2196f3;
}

/* 捐赠按钮特定样式 */
.donate-button {
  background-color: #ff5722;
  border-radius: 15rpx;
  transition: background-color 0.3s, transform 0.3s;
}

.donate-button:hover {
  background-color: #e64a19;
}

.donate-button:active {
  transform: scale(0.95);
}

/* 响应式设计 */
@media (max-width: 600rpx) {
  .info-card {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }

  .avatar {
    margin-right: 0;
    margin-bottom: 20rpx;
  }

  .user-stats {
    justify-content: center;
  }

  .stat-item {
    margin-right: 20rpx;
  }

  .tools-row {
    flex-direction: column;
    align-items: center;
  }

  .tool-item {
    width: 80%;
    margin-bottom: 20rpx;
  }
}
</style>
