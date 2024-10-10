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

    <!-- 设置界面按钮 -->
    <view class="settings-container">
      <button class="settings-button" @click="modifyProject">
        <image src="/static/icons/edit.png" class="button-icon" />
        修改项目
      </button>
      <button class="settings-button delete-button" @click="deleteProject">
        <image src="/static/icons/delete.png" class="button-icon" />
        删除该项目
      </button>
    </view>
  </view>
</template>


<script>
export default {
  data() {
    return {
      tabs: ['项目信息', '项目成员', '项目设置'],
      activeTab: 2,
      projectId: '' // 存储项目 ID
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
		console.log(projectId);
    
        if (index === 0) {
          uni.redirectTo({
            url: `/pages/home/look?id=${this.projectId}` // 将 projectId 传递给 look 页面
          });
        } else if (index === 1) {
          uni.redirectTo({
            url: `/pages/home/teammate?id=${this.projectId}` // 将 projectId 传递给 teammate 页面
          });
        }
      },
    modifyProject() {
      // 点击“修改项目”后跳转到发布项目页面
      uni.navigateTo({
        url: '/pages/home/publish_project'
      });
    },
    deleteProject() {
      // 删除项目的逻辑，可以添加确认弹窗
      uni.showModal({
        title: '确认删除',
        content: '您确定要删除该项目吗？',
        success: (res) => {
          if (res.confirm) {
            const token = uni.getStorageSync('authToken'); // 获取存储的 token

            // 执行删除操作的 API 请求
            uni.request({
              url: `https://734dw56037em.vicp.fun/projects/projects/${this.projectId}/`,
              method: 'DELETE',
              header: {
                'Authorization': `Token ${token}`,
                'Content-Type': 'application/json'
              },
              success: (response) => {
                if (response.statusCode === 204) { // 成功删除
                  uni.showToast({
                    title: '项目已删除',
                    icon: 'success'
                  });
                  // 删除后跳转到首页或其他页面
                  uni.switchTab({
                    url: '/pages/home/home'
                  });
                } else {
                  uni.showToast({
                    title: '删除项目失败',
                    icon: 'none'
                  });
                }
              },
              fail: (err) => {
                console.error('请求失败:', err);
                uni.showToast({
                  title: '请求失败，请稍后再试',
                  icon: 'none'
                });
              }
            });
          }
        }
      });
    }
  },
  mounted() {
    // 在这里获取项目 ID，假设通过页面参数传递
    const pages = getCurrentPages();
    const currentPage = pages[pages.length - 1];
    this.projectId = currentPage.options.projectId; // 从页面参数获取 projectId
  }
};
</script>


<style scoped>
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

/* 设置界面按钮样式 */
.settings-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.settings-button {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #fff;
  color: #333;
  border: none;
  border-radius: 12rpx;
  padding: 20rpx 40rpx;
  font-size: 32rpx;
  box-shadow: 0 4rpx 8rpx rgba(0, 0, 0, 0.1);
  margin-bottom: 30rpx;
  cursor: pointer;
  width: 60%;
}

.button-icon {
  width: 40rpx;
  height: 40rpx;
  margin-right: 20rpx;
}

.delete-button {
  background-color: #ff3b30;
  color: #fff;
}

.delete-button .button-icon {
  filter: invert(1);
}
</style>
