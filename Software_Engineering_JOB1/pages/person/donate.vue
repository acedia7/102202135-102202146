<template>
  <view class="donate-container">
    <!-- 页面标题 -->
    <view class="donate-header animated fadeInDown">
      <text class="donate-title">支持我们，您的捐赠是我们前进的动力！</text>
    </view>

    <!-- 二维码展示区 -->
    <view class="qr-code-container animated fadeInUp delay-1s">
      <image :src="qrCode" class="qr-code" />
      <text class="qr-instruction">请扫描二维码进行捐赠</text>
    </view>

    <!-- 捐赠说明 -->
    <view class="donate-description animated fadeInUp delay-2s">
      <text class="description-text">
        感谢您的支持！您的每一份捐赠都将用于平台的维护和优化，帮助我们为您和更多用户提供更好的服务。
      </text>
    </view>

    <!-- 返回按钮 -->
    <view class="back-button-container animated fadeInUp delay-3s">
      <button class="back-button" @click="goBack">返回</button>
    </view>
  </view>
</template>
<script>
export default {
  data() {
    return {
      // 捐赠二维码的路径
      qrCode: '/static/photo/donate.jpg', // 请确保该路径下有你的二维码图片
    };
  },
  methods: {
    goBack() {
      uni.navigateBack({
        delta: 1, // 返回上一级页面
      });
    },
  },
};
</script>
<style scoped>
/* 定义动画关键帧 */
@keyframes fadeInDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

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

/* 动画类 */
.animated {
  animation-duration: 1s;
  animation-fill-mode: both;
}

.fadeInDown {
  animation-name: fadeInDown;
}

.fadeInUp {
  animation-name: fadeInUp;
}

.delay-1s {
  animation-delay: 1s;
}

.delay-2s {
  animation-delay: 2s;
}

.delay-3s {
  animation-delay: 3s;
}

/* 容器样式 */
.donate-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  /* 移除背景颜色和渐变 */
  /* background: linear-gradient(-45deg, #f5f7fa, #c3cfe2, #a1c4fd, #c2e9fb); */
  /* background-size: 400% 400%; */
  /* animation: backgroundGradient 15s ease infinite; */
  padding: 40rpx;
  min-height: 100vh;
  box-sizing: border-box;
}

/* 页面标题样式 */
.donate-header {
  margin-bottom: 40rpx;
}

.donate-title {
  font-size: 36rpx;
  color: #333333;
  text-align: center;
  font-weight: bold;
  text-shadow: 1rpx 1rpx 2rpx rgba(0, 0, 0, 0.1);
}

/* 二维码展示区样式 */
.qr-code-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 40rpx;
}

.qr-code {
  width: 500rpx; /* 增大二维码尺寸 */
  height: 650rpx; /* 保持原始比例 */
  border: 4rpx solid #2196f3;
  border-radius: 20rpx;
  box-shadow: 0 4rpx 16rpx rgba(0, 0, 0, 0.1);
  transition: transform 0.3s, box-shadow 0.3s;
}

.qr-code:hover {
  transform: scale(1.05);
  box-shadow: 0 8rpx 24rpx rgba(0, 0, 0, 0.2);
}

.qr-instruction {
  font-size: 28rpx;
  color: #555555;
  margin-top: 20rpx;
  text-align: center;
}

/* 捐赠说明样式 */
.donate-description {
  max-width: 800rpx;
  padding: 20rpx;
  background-color: rgba(255, 255, 255, 0.8);
  border-radius: 20rpx;
  box-shadow: 0 4rpx 16rpx rgba(0, 0, 0, 0.1);
  transition: transform 0.3s, box-shadow 0.3s;
}

.donate-description:hover {
  transform: translateY(-5rpx);
  box-shadow: 0 8rpx 24rpx rgba(0, 0, 0, 0.2);
}

.description-text {
  font-size: 28rpx;
  color: #333333;
  text-align: center;
  line-height: 1.5;
}

/* 返回按钮样式 */
.back-button-container {
  margin-top: 40rpx;
}

.back-button {
  width: 200rpx;
  height: 60rpx;
  background-color: #2196f3;
  color: #ffffff;
  border: none;
  border-radius: 30rpx;
  font-size: 28rpx;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s;
  box-shadow: 0 4rpx 12rpx rgba(0, 0, 0, 0.1);
}

.back-button:hover {
  background-color: #1976d2;
}

.back-button:active {
  transform: scale(0.95);
}

/* 响应式设计 */
@media (max-width: 600rpx) {
  .donate-title {
    font-size: 28rpx;
  }

  .qr-code {
    width: 300rpx;
    height: 300rpx;
  }

  .qr-instruction {
    font-size: 24rpx;
  }

  .description-text {
    font-size: 24rpx;
  }

  .back-button {
    width: 150rpx;
    height: 50rpx;
    font-size: 24rpx;
  }
}
</style>
