<template>
  <view class="container">
    <!-- 反馈表单 -->
    <view class="feedback-form">
      <!-- 反馈类型选择 -->
      <view class="form-item">
        <text class="label">反馈类型</text>
        <picker mode="selector" :range="feedbackTypes" @change="onTypeChange">
          <view class="picker">
            <text class="picker-text">{{ selectedType }}</text>
            <image src="/static/icons/arrow_down.png" class="arrow-icon" />
          </view>
        </picker>
      </view>

      <!-- 反馈内容输入 -->
      <view class="form-item">
        <text class="label">反馈内容</text>
        <textarea 
          v-model="feedbackContent" 
          placeholder="请详细描述您的问题或建议..." 
          class="textarea" 
          auto-height
        ></textarea>
      </view>

      <!-- 联系方式输入（可选） -->
      <view class="form-item">
        <text class="label">联系方式（可选）</text>
        <input 
          v-model="contactInfo" 
          placeholder="您的邮箱或电话" 
          class="input" 
          type="text"
        />
      </view>

      <!-- 提交按钮 -->
      <button class="submit-button" @click="submitFeedback">提交反馈</button>
    </view>

    <!-- 成功提示弹窗 -->
    <view v-if="showSuccess" class="success-popup">
      <image src="/static/icons/success.png" class="success-icon" />
      <text class="success-text">感谢您的反馈！</text>
      <button class="close-button" @click="closePopup">关闭</button>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      feedbackTypes: ['建议', '问题', '其他'],
      selectedType: '请选择反馈类型',
      feedbackContent: '',
      contactInfo: '',
      showSuccess: false
    };
  },
  methods: {
    onTypeChange(e) {
      const index = e.detail.value;
      this.selectedType = this.feedbackTypes[index];
    },
    submitFeedback() {
      if (this.selectedType === '请选择反馈类型') {
        uni.showToast({
          title: '请选择反馈类型',
          icon: 'none'
        });
        return;
      }
      if (!this.feedbackContent.trim()) {
        uni.showToast({
          title: '请填写反馈内容',
          icon: 'none'
        });
        return;
      }

      // 模拟提交反馈
      // 在实际项目中，这里应该调用API接口提交反馈数据
      console.log({
        type: this.selectedType,
        content: this.feedbackContent,
        contact: this.contactInfo
      });

      // 清空表单
      this.feedbackContent = '';
      this.contactInfo = '';
      this.selectedType = '请选择反馈类型';

      // 显示成功提示
      this.showSuccess = true;
    },
    closePopup() {
      this.showSuccess = false;
    }
  }
};
</script>


<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #f0f2f5;
  padding: 40rpx 20rpx;
  min-height: 100vh;
  box-sizing: border-box;
}

/* 反馈表单样式 */
.feedback-form {
  width: 100%;
  max-width: 800rpx;
  background-color: #ffffff;
  border-radius: 20rpx;
  padding: 30rpx 40rpx;
  box-shadow: 0 4rpx 16rpx rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.form-item {
  width: 100%;
  margin-bottom: 25rpx;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.label {
  align-self: flex-start;
  font-size: 32rpx; /* 增大字体大小 */
  font-weight: bold; /* 加粗 */
  color: #555555;
  margin-bottom: 10rpx;
  width: 100%;
}

.picker {
  width: 100%; /* 统一宽度 */
  display: flex;
  justify-content: space-between;
  align-items: center;
  border: 1rpx solid #dddddd;
  border-radius: 10rpx;
  padding: 15rpx 20rpx;
  background-color: #f9f9f9;
}

.picker-text {
  font-size: 26rpx;
  color: #333333;
}

.arrow-icon {
  width: 24rpx;
  height: 24rpx;
}

.textarea {
  width: 100%;
  height: 400rpx; /* 进一步增大高度 */
  min-height: 400rpx; /* 设置最小高度 */
  border: 1rpx solid #dddddd;
  border-radius: 10rpx;
  padding: 15rpx;
  font-size: 26rpx;
  color: #333333;
  background-color: #f9f9f9;
  resize: vertical; /* 允许垂直方向调整高度 */
  box-sizing: border-box;
}

.input {
  width: 100%;
  height: 50rpx;
  border: 1rpx solid #dddddd;
  border-radius: 10rpx;
  padding: 15rpx;
  font-size: 26rpx;
  color: #333333;
  background-color: #f9f9f9;
  box-sizing: border-box;
}

.submit-button {
  width: 100%;
  max-width: 300rpx;
  height: 60rpx;
  background-color: #007aff;
  color: #ffffff;
  font-size: 28rpx;
  border: none;
  border-radius: 10rpx;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s;
  margin-top: 10rpx;
}

.submit-button:hover {
  background-color: #005bb5;
  transform: scale(1.02);
}

/* 成功提示弹窗样式 */
.success-popup {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #ffffff;
  border-radius: 20rpx;
  padding: 40rpx 30rpx;
  box-shadow: 0 4rpx 16rpx rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  align-items: center;
  z-index: 1000;
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
  transform: scale(1.02);
}

/* 响应式设计 */
@media (max-width: 600rpx) {
  .feedback-form {
    padding: 20rpx;
  }

  .label {
    font-size: 24rpx;
  }

  .picker-text,
  .textarea,
  .input,
  .submit-button,
  .close-button {
    font-size: 24rpx;
  }

  .textarea {
    height: 220rpx; /* 略微减小以适应小屏设备 */
  }

  .submit-button {
    max-width: 100%;
  }
}
</style>
