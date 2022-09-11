<template>
    <el-form 
      :model="form"
      :rules="rules"
      ref="form"
      class="businessRegisterMain3" 
    >
      <el-form-item class = "successItem">
        <el-icon color="green" size = "large"><SuccessFilled /></el-icon>
        <h3>提交成功！</h3>
      </el-form-item>

      <p class = "successDetail">请耐心等待审核消息</p>

      <el-form-item class = "businessWaitingImageClass">
        <img alt="businessWaitingLogo" src="../../assets/waitingLogo.svg" class = "businessWaitingImage">
      </el-form-item>
  
      
  
      <el-form-item class = "loginLink">
        <el-row class = "row">
        <el-col :span="12">  
            <el-link :underline="false">
            登录账号
          </el-link>
          </el-col>
        <el-col :span="12">
          <el-link :underline="false">
            返回首页
          </el-link>
        </el-col>
      </el-row>
          
      </el-form-item>
    </el-form>
  
</template>

<script>
export default {
  name: 'businessRegisterMain3',
  components: {
  }
}
</script>



<style>
.businessRegisterMain3 {
  margin-right:0px;
  width:100%;
  height: 380px;
}

.successItem {
  margin-left: 45%;
  margin-bottom: 0%;
  height: 40px;
}

.successDetail {
  text-align: center;
  margin-top: 0%;
  font-family: "微软雅黑";
  font-weight:bold;
  color :#606266;
}

.businessWaitingImage {
  height: 250px;
  width: 250px;
}


.businessRegisterImageFormClass {
  margin: auto;
}

.businessWaitingImageClass {
  margin-left:37%;
}

.el-link {
    margin-right: 8px;
}
.el-link .el-icon--right.el-icon {
    vertical-align: text-bottom;
}

.loginLink {
    width: 300px;
    margin: 0px 0px 0px 335px;
    padding: 0px 0px 0px auto;
    padding-left: 35px;
}


</style>