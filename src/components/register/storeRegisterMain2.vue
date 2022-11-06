<!-- storeRegisterCard2的子组件，负责获得商家营业执照
其包含子组件storeRegisterLeft2——负责获得商家商家注册的店铺地址，店铺介绍，店铺头像 -->

<!-- TODO:
提交按钮：根据后端返回值
1.“信息不完整”出现弹窗
2.“提交成功”发送一个信号给storeRegisterCard2，storeRegisterCard2再传信号给storeRegisterPage，然后storeRegisterPage会切换到storeRegisterCard3组件

登录账号按钮：跳转到storeRegisterPage

返回首页按钮：跳转到firstPage -->

<template>
    
    <el-row
    style = "margin-right:0px;
            width:100%;">
      <el-col :span="12" class = "storeRegisterFormCol">
        <el-form 
          :model="form"
          :rules="rules"
          ref="form"
          class="storeRegisterLeft2" 
        >
          <el-form-item prop="address" class = "shopAddressInputBox">
            <el-input
              v-model="input"
              type="address"
              placeholder="店铺地址"
              size = "large"
              style = "width: 300px;
                margin-top: 10px;
                margin-left: auto;
                margin-right: auto;
                margin-bottom: 10px;
                height: 45px;"
            
            >
              <template #prefix>
                <el-icon class="el-input__icon"><location /></el-icon>
              </template>
            </el-input>
      
          </el-form-item>

          <el-form-item prop="intro" class = "introInputBox"
            style="width: 300px;
                    margin-bottom: 10px;
                    margin-left: auto;
                    margin-right: auto;
                    margin-top: 20px;
                    height: 70px;">
            <el-input
                v-model="textarea2"
                :autosize="{ minRows: 3, maxRows: 4 }"
                type="textarea"
                placeholder="店铺介绍"
            >
            
            </el-input>
          </el-form-item>


          <el-form-item 
          style = "margin-top :5%;
                  margin-left:15%;
                  width: 300px;">
            <el-row style = "width: 300px;">


              <el-col :span="12">
                <p
                style = "text-align: center;
                      font-size: 15px;
                      margin-left:20%;
                      font-weight: bold;
                      color:#606266;">
          上传店铺头像</p>
              </el-col>


              <el-col :span="12">
                <el-upload
                class="avatar-uploader-head"
                action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
                :show-file-list="false"
                :on-success="handleAvatarSuccess"
                :before-upload="beforeAvatarUpload"
                >
                  <img v-if="imageUrl" :src="imageUrl" class="avatar" />
                  <el-icon v-else class="logo-uploader-icon"><Plus /></el-icon>
                </el-upload>
              </el-col>


            </el-row>

          </el-form-item>

          
          <el-form-item
          style="width: 300px;
          margin-top:2%;
          margin-left: auto;
          margin-right: auto;">
      
            <el-button 
              color = "#fec01b" 
              round
              plain
              size = "large"
              style="width: 300px;
                margin-top:2%;
                margin-left: auto;
                margin-right: auto;"
            >
              提交申请
            </el-button>
      
          </el-form-item>

          
      
          <el-form-item style = "margin-left: 130px;width: 300px;
          margin-left: 30%;
          padding: 0;
          margin-bottom: 0;">
            
            <el-row style = " width : 350px">
            <el-col :span="12">  
                <el-link :underline="false" style = "margin-right: 8px;">
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
      </el-col>


      <el-col :span="12" class = "storeRegisterImageFormCol">
        <el-upload
            class="avatar-uploader-license"
            action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
            :show-file-list="false"
            :on-success="handleAvatarSuccess"
            :before-upload="beforeAvatarUpload"
        >
            <img v-if="imageUrl" :src="imageUrl" class="avatar" />
            <el-icon v-else class="license-uploader-icon"><Plus /></el-icon>
        </el-upload>

        <p class = "uploadDetail">上传营业执照</p>


      </el-col>


    </el-row>
  
</template>

<script>
export default {
  name: 'storeRegisterMain2',
  components: {
  }
}
</script>



<style>
/* .storeRegisterRow {
  margin-right:0px;
  width:100%;
} */


.storeRegisterLeft2 {
  margin:auto;
  
}

.storeRegisterImageFormClass {
  margin: auto;
}


.avatar-uploader-license .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }
  .avatar-uploader-license {
    margin-left:150px;
  }

  .storeRegisterRight2 {
    width: 400px;
    height: 350px;
    /*padding: 30px;*/
    border-radius: 20px;
    /* 整个表单el-form位于整个屏幕的位置 margin */  

  }
  .storeRegisterRightItem {
    margin-top: 0%;
    margin-left: 20%;
    
  }

  .uploadDetail {
    text-align: center;
    font-size: 18px;
    margin-left:20%;
    font-weight: bold;
    color:#606266;
  }

    .avatar-uploader-license .el-upload {
    border: 1px dashed var(--el-border-color);
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    transition: var(--el-transition-duration-fast);
  }
  
  .avatar-uploader-license .el-upload:hover {
    border-color: var(--el-color-primary);
  }
  
  .el-icon.license-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 250px;
    height: 300px;
    text-align: center;
  }


</style>