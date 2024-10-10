<template>
  <view class="container">
    <!-- 顶部导航栏 -->
    <view class="navbar">
      <text
        v-for="(tab, index) in tabs"
        :key="index"
        :class="['navbar-tab', { active: activeTab === index }]"
        @click="switchTab(index)"
      >
        {{ tab }}
      </text>
    </view>
    <view class="navbar-line"></view>

    <!-- 发布者信息 -->
    <view class="card-container">
      <view class="card">
        <view class="card-header">
          <image src="/static/icons/publisher.png" class="card-icon" />
          <text class="card-title">发布者</text>
        </view>
        <view class="card-content">
          <view class="info-item">
            <text class="info-label">姓名：</text>
            <text class="info-text">{{ publisher.name }}</text>
          </view>
          <view class="info-item">
            <text class="info-label">兴趣领域：</text>
            <text class="info-text">{{ publisher.interest }}</text>
          </view>
        </view>
      </view>
    </view>

    <!-- 参与者信息 -->
    <view class="card-container">
      <view class="card">
        <view class="card-header">
          <image src="/static/icons/participant.png" class="card-icon" />
          <text class="card-title">参与者</text>
        </view>
        <scroll-view class="card-content" scroll-y="true" :style="{ maxHeight: '400rpx' }">
          <view class="participant-item" v-for="(participant, index) in participants" :key="index">
            <view class="info-item">
              <text class="info-label">姓名：</text>
              <text class="info-text">{{ participant.name }}</text>
            </view>
            <view class="info-item">
              <text class="info-label">兴趣领域：</text>
              <text class="info-text">{{ participant.interest }}</text>
            </view>
          </view>
        </scroll-view>
      </view>
    </view>

    <!-- 指导老师信息 -->
    <view class="card-container">
      <view class="card">
        <view class="card-header">
          <image src="/static/icons/mentor.png" class="card-icon" />
          <text class="card-title">导师</text>
        </view>
        <scroll-view class="card-content" scroll-y="true" :style="{ maxHeight: '400rpx' }">
          <view class="mentor-item" v-for="(mentor, index) in mentors" :key="index">
            <view class="info-item">
              <text class="info-label">姓名：</text>
              <text class="info-text">{{ mentor.name }}</text>
            </view>
            <view class="info-item">
              <text class="info-label">擅长领域：</text>
              <text class="info-text">{{ mentor.expertise }}</text>
            </view>
          </view>
        </scroll-view>
      </view>
    </view>

    <!-- 招募和请求按钮 -->
    <view class="button-container">
      <button class="recruit-button" @click="recruitCollaborator">
        <image src="/static/icons/recruit.png" class="button-icon" />
        招募合作者
      </button>
      <button class="request-button" @click="requestMentor">
        <image src="/static/icons/request.png" class="button-icon" />
        请求导师
      </button>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      tabs: ['项目信息', '项目成员', '项目设置'],
      activeTab: 1,
      publisher: {
        name: '发布者姓名',
        interest: '发布者兴趣领域',
      },
      participants: [
        { name: '参与者1', interest: '兴趣领域1' },
        { name: '参与者2', interest: '兴趣领域2' },
		{ name: '参与者2', interest: '兴趣领域2' },
		{ name: '参与者2', interest: '兴趣领域2' },
		{ name: '参与者2', interest: '兴趣领域2' },
		{ name: '参与者2', interest: '兴趣领域2' },
		{ name: '参与者1', interest: '兴趣领域1' },
		{ name: '参与者2', interest: '兴趣领域2' },
		{ name: '参与者2', interest: '兴趣领域2' },
		{ name: '参与者2', interest: '兴趣领域2' },
		{ name: '参与者2', interest: '兴趣领域2' },
		{ name: '参与者2', interest: '兴趣领域2' },
        // 可以继续添加更多参与者
      ],
      mentors: [
        { name: '导师1', expertise: '擅长领域1' },
        { name: '导师2', expertise: '擅长领域2' },
        // 可以继续添加更多导师
      ],
    };
  },
  onLoad(options) {
    this.projectId = options.id; // 从页面参数获取项目 id
    console.log('Project ID:', this.projectId); // 输出查看
    this.getProjectFiles(); // 获取项目文件
  },
  methods: {
    switchTab(index) {
        this.activeTab = index;
    
        if (index === 0) {
          uni.redirectTo({
            url: `/pages/home/look?id=${this.projectId}`, // 将 projectId 传递给 look 页面
          });
        } else if (index === 2) {
          uni.redirectTo({
            url: `/pages/home/project_setting?id=${this.projectId}`, // 将 projectId 传递给 project_setting 页面
          });
        }
      },
    recruitCollaborator() {
      // 招募合作者的逻辑
      console.log('招募合作者');
    },
    requestMentor() {
      // 请求导师的逻辑
      console.log('请求导师');
    },
  },
};
</script>

<style>
.container {
  display: flex;
  flex-direction: column;
  background-color: #f0f4f7;
  padding: 0;
  height: 100vh;
}

/* 顶部导航栏样式 */
.navbar {
  display: flex;
  justify-content: space-around;
  align-items: center;
  background-color: #ffffff;
  padding-top: 20rpx;
  padding-bottom: 20rpx;
}

.navbar-tab {
  font-size: 32rpx;
  color: #666;
  cursor: pointer;
}

.navbar-tab.active {
  color: #007aff;
  font-weight: bold;
}

.navbar-line {
  width: 100%;
  height: 2rpx;
  background-color: #e0e0e0;
}

/* 卡片样式 */
.card-container {
  margin: 20rpx 20rpx;
}

.card {
  background-color: #ffffff;
  border-radius: 20rpx;
  box-shadow: 0 4rpx 8rpx rgba(0, 0, 0, 0.1);
  padding: 20rpx;
}

.card-header {
  display: flex;
  align-items: center;
  margin-bottom: 10rpx;
}

.card-icon {
  width: 50rpx;
  height: 50rpx;
  margin-right: 10rpx;
}

.card-title {
  font-size: 32rpx;
  font-weight: bold;
}

.card-content {
  display: flex;
  flex-direction: column;
}

.info-item {
  display: flex;
  flex-direction: row;
  margin-bottom: 10rpx;
}

.info-label {
  width: 200rpx;
  font-size: 28rpx;
  color: #333;
}

.info-text {
  flex: 1;
  font-size: 28rpx;
  color: #666;
}

/* 参与者和导师项 */
.participant-item,
.mentor-item {
  padding-bottom: 10rpx;
  border-bottom: 1rpx solid #e0e0e0;
  margin-bottom: 10rpx;
}

/* 招募和请求按钮样式 */
.button-container {
  display: flex;
  justify-content: space-around;
  margin: 30rpx 20rpx;
}

.recruit-button,
.request-button {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #007aff;
  color: #fff;
  border: none;
  border-radius: 12rpx;
  padding: 20rpx;
  font-size: 32rpx;
  box-shadow: 0 4rpx 8rpx rgba(0, 0, 0, 0.1);
  cursor: pointer;
  width: 45%;
}

.button-icon {
  width: 40rpx;
  height: 40rpx;
  margin-right: 10rpx;
}
</style>
