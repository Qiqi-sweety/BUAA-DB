<template>
    <el-row class = "introRow">
        <el-col :span="13" class = "intro1Col">
            <h3 class = "introTitle">
                贪吃不胖
            </h3>
            <p class = "introDetail">
                    外卖小站
            </p>
  
        </el-col>
        <el-col :span="11" class = "intro2Col">
            <img alt="fastFood" src="../../assets/fastFood.svg" class = "bigLogo" >
            <img alt="noodle" src="../../assets/noodle.svg" class = "bigLogo" >
            <img alt="Meal" src="../../assets/Meal.svg" class = "bigLogo" >
                
            <img alt="Sandwich" src="../../assets/Sandwich.svg" class = "bigLogo" >
            <img alt="Pancake" src="../../assets/Pancake.svg" class = "bigLogo" >
            <img alt="Steak" src="../../assets/Steak.svg" class = "bigLogo" >
        </el-col>
    </el-row>
</template>

<script>

export default {
  name: 'intro',
  components: {
   
  }
}
</script>

<style>

.introRow {
    padding-bottom: 0px;
    height: 455px;
    width: 100%;
}

.introTitle {
    /* border: 1px solid black; */
    margin-left: 200px;
    font-size :120px;
    width:500px;
    margin-bottom: 10px;
    margin-top:50px

}

.introDetail {
    /* border: 1px solid black; */
    font-size: 80px;
    margin-top:0px;
    margin-left: 500px;
    color :#606266;
    font-family: "微软雅黑";
    font-weight:bold;
}


.bigLogo {
    height: 200px;
    width: 200px;
    margin-bottom: 0px;
}
</style>