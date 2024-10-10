<template>
  <view class="failure-container">
    <!-- 背景遮罩 -->
    <view class="background-overlay"></view>

    <!-- 失败提示框 -->
    <view class="failure-box">
      <view class="message-header">
        <text class="message-text">注册失败</text>
      </view>
      <view class="message-body">
        <text class="instruction-text">请检查邮箱是否正确，验证码是否有误，以及您是否已拥有账户</text>
      </view>
      <view class="confirm-button-container">
        <button type="primary" @click="handleConfirm" class="confirm-button">确认</button>
      </view>
    </view>
  </view>
</template>

<script>
export default {
  name: "RegisterFailure",
  methods: {
    handleConfirm() {
      // 返回注册页面逻辑
      uni.navigateTo({
        url: '/pages/register/register'
      });
    }
  }
};
</script>

<style scoped>
.failure-container {
  position: relative;
  width: 100%;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #333;
}

.background-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  z-index: -1;
}

.failure-box {
  width: 80%;
  background-color: #fff;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  text-align: center;
}

.message-header {
  margin-bottom: 10px;
}

.message-text {
  font-size: 1.5rem;
  font-weight: bold;
}

.message-body {
  margin-bottom: 20px;
}

.instruction-text {
  font-size: 1rem;
  color: #666;
}

.confirm-button-container {
  margin-top: 10px;
}

.confirm-button {
  width: 100%;
  padding: 10px;
  background-color: #e74c3c;
  color: #fff;
  border: none;
  border-radius: 5px;
  font-size: 16px;
}
</style>