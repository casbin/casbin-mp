from manim import *

class Video(Scene):
    def construct(self):
        ##logo引入
        casbin_pic = ImageMobject("pictures/casbin.png")
        self.play(FadeIn(casbin_pic, scale=0.6))
        self.play(casbin_pic.animate.scale(0.6))
        self.play(casbin_pic.animate.to_corner(UL))

        ##什么是Casdoor
        caption1 = Text("什么是Casdoor?")
        self.play(Write(caption1), shift=DOWN)
        self.wait(1)
        self.play(caption1.animate.to_edge(DOWN))
        self.play(FadeOut(caption1))

        ##特性快闪
        features0 = Text("身份验证").scale(2).set_color(RED)
        features1 = Text("单点登录").scale(2).set_color(YELLOW)
        features2 = Text("OAuth 2.0").scale(2).set_color(BLUE)
        features3 = Text("OIDC").scale(2).set_color(GREEN)
        self.play(FadeIn(features0))
        self.play(FadeOut(features0))
        self.play(FadeIn(features1))
        self.play(FadeOut(features1))
        self.play(FadeIn(features2))
        self.play(FadeOut(features2))
        self.play(FadeIn(features3))
        self.play(FadeOut(features3))

        ###特色介绍
        why_choose = Text("为什么要选择Casdoor?").scale(2)
        self.play(Write(why_choose))
        self.play(FadeOut(why_choose))

        signin = ImageMobject("pictures/signin.png")
        signintext1 = Text("Casdoor支持账户密码登录")
        signintext2 = Text("支持多平台认证登录")
        signintext1.to_edge(RIGHT)
        signintext2.next_to(signintext1, DOWN)
        signin.to_edge(LEFT)
        signintextgroup = [
            FadeIn(signintext1),
            FadeIn(signintext2)
        ]
        self.play(FadeIn(signin))
        self.play(*signintextgroup)

        signingroup =[
            FadeOut(signin),
            FadeOut(signintext1),
            FadeOut(signintext2)
        ]
        self.play(*signingroup)

        ######管理方便
        organizations = ImageMobject("pictures/organizations.png")
        users = ImageMobject("pictures/users.png")
        providers = ImageMobject("pictures/providers.png")
        applications = ImageMobject("pictures/applications.png")

        organizations.to_edge(UP)
        users.next_to(organizations, RIGHT)
        providers.next_to(organizations, DOWN)
        applications.next_to(users, DOWN)

        homecontent = [
            FadeIn(organizations),
            FadeIn(users),
            FadeIn(providers),
            FadeIn(applications)
        ]
        self.play(*homecontent)

        homecaption = Text("内部模块化， 轻松管理复杂系统")
        homecaption.to_edge(DOWN)
        self.play(FadeIn(homecaption))

        homecontentclear = [
            FadeOut(organizations),
            FadeOut(users),
            FadeOut(providers),
            FadeOut(applications),
            FadeOut(homecaption)
        ]
        self.play(*homecontentclear)


        ######多语言支持
        multilangue = Text("多语言支持").scale(1.4)
        hellocn = Text("你好").set_color(RED).scale(2)
        hellofr = Text("Bonjour").set_color(ORANGE).scale(2)
        hellode = Text("Hallo").set_color(YELLOW).scale(2)
        helloen = Text("Hello").set_color(GREEN).scale(2)
        hellojp = Text("こんにちは").set_color(PINK).scale(2)
        helloru = Text("привет").set_color(BLUE).scale(2)
        hellokr = Text("안녕하세요").set_color(PURPLE).scale(2)

        ###设置多语言位置
        hellocn.to_edge(UP)
        helloru.to_corner(UR)
        helloen.next_to(multilangue, RIGHT)
        hellokr.next_to(multilangue, DOWN)
        hellofr.to_edge(DOWN)
        hellode.next_to(multilangue, LEFT)
        hellojp.next_to(multilangue, UP)

        ##浮现多语言
        self.play(Write(multilangue))
        self.play(FadeIn(hellocn)),
        self.play(FadeIn(helloen)),
        self.play(FadeIn(hellofr)),
        self.play(FadeIn(hellode)),
        self.play(FadeIn(helloru)),
        self.play(FadeIn(hellojp)),
        self.play(FadeIn(hellokr))

        ##清屏
        helloclear = [
        FadeOut(multilangue),
        FadeOut(hellocn),
        FadeOut(helloen),
        FadeOut(hellofr),
        FadeOut(hellode),
        FadeOut(helloru),
        FadeOut(hellojp),
        FadeOut(hellokr)
        ]
        self.play(*helloclear)

##############################################################################################
        #################原理介绍
        ##各个provider引入
        github = ImageMobject("pictures/github.png")
        google = ImageMobject("pictures/google.png")
        qq = ImageMobject("pictures/qq.png")
        wechat = ImageMobject("pictures/wechat.png")
        gitee = ImageMobject("pictures/gitee.png")
        linkedin = ImageMobject("pictures/linkedin.png")
        twitter = ImageMobject("pictures/twitter.png")
        facebook = ImageMobject("pictures/facebook.png")
        wecom = ImageMobject("pictures/wecom.png")
        lark = ImageMobject("pictures/lark.png")
        weibo = ImageMobject("pictures/weibo.png")
        gitlab = ImageMobject("pictures/gitlab.png")

        ##用户引入
        gopher = ImageMobject("pictures/gopher.png")
        gopher.to_edge(LEFT)
        user = Text("用户").scale(0.6)
        user.next_to(gopher, UP)

        ##资源引入
        resource = ImageMobject("pictures/resource.png")
        resource.to_edge(UP)

        ###provider的位置设定
        github.shift(5*RIGHT+DOWN)
        google.next_to(github, UP)
        qq.next_to(google, UP)
        wechat.next_to(github, DOWN)
        gitee.next_to(wechat, DOWN)
        linkedin.next_to(qq, RIGHT)
        twitter.next_to(google, RIGHT)
        facebook.next_to(github, RIGHT)
        wecom.next_to(wechat, RIGHT)
        lark.next_to(gitee, RIGHT)
        weibo.next_to(qq, UP)
        gitlab.next_to(linkedin, UP)

        theory = Text("原理解析")
        self.play(FadeIn(theory))
        self.play(FadeOut(theory))

        supply = Text("提供商").scale(0.6)
        supply.next_to(weibo, UP)

        resources = Text("要访问的资源").scale(0.6)
        resources.next_to(resource, LEFT)
        resources.to_edge(UP)

        providergroup =[
        FadeIn(weibo),
        FadeIn(gitlab),
        FadeIn(qq),
        FadeIn(linkedin),
        FadeIn(google),
        FadeIn(twitter),
        FadeIn(github),
        FadeIn(facebook),
        FadeIn(wechat),
        FadeIn(wecom),
        FadeIn(gitee),
        FadeIn(lark)
        ]
        self.play(*providergroup)


        gophergroup =[
            FadeIn(gopher, scale=0.8),
            FadeIn(user)
        ]
        self.play(*gophergroup)

        self.play(casbin_pic.animate.move_to(DOWN))
        self.play(casbin_pic.animate.scale(2))
        casdoor = Text("Casdoor").scale(0.6)
        casdoor.next_to(casbin_pic, DOWN)
        self.play(FadeIn(casdoor))
        self.play(FadeIn(supply))

        self.play(FadeIn(resource, scale = 1.3))
        self.play(FadeIn(resources))

        ###资源访问的过程
        casdoortouser = Arrow(start=LEFT+DOWN, end=4*LEFT)
        request = Text("请确认身份🤖").scale(0.6)
        request.next_to(casdoortouser, UP)
        self.play(Create(casdoortouser, runtime=6))
        self.play(FadeIn(request))

        requestout =[
            FadeOut(casdoortouser),
            FadeOut(request)
        ]
        self.play(*requestout)

        ####
        usertocasdoor = Arrow(start=4*LEFT, end=LEFT+DOWN)
        credential = Text("我是Gopher！🔑").scale(0.6)
        credential.next_to(usertocasdoor, UP)
        self.play(Create(usertocasdoor))
        self.play(FadeIn(credential))
        requestin =[
            FadeOut(usertocasdoor),
            FadeOut(credential)
        ]
        self.play(*requestin)


        ###Casdoor到第三方
        casdoortothird = Arrow(start=RIGHT+DOWN, end=5*RIGHT)
        casdoortothirdtext = Text("这里是Gopher🔑").scale(0.6)
        casdoortothirdtext.next_to(casdoortothird, DOWN)
        self.play(Create(casdoortothird))
        self.play(FadeIn(casdoortothirdtext))
        casdoortothirdgroup =[
            FadeOut(casdoortothird),
            FadeOut(casdoortothirdtext)
        ]
        self.play(*casdoortothirdgroup)


        ###第三方到Casdoor
        thirdtocasdoor = Arrow(start=5*RIGHT, end=RIGHT+DOWN)
        thirdtocasdoortext = Text("确认是Gopher✔").scale(0.6)
        thirdtocasdoortext.next_to(thirdtocasdoor, DOWN)
        self.play(Create(thirdtocasdoor))
        self.play(FadeIn(thirdtocasdoortext))
        thirdtocasdoorgroup =[
            FadeOut(thirdtocasdoor),
            FadeOut(thirdtocasdoortext)
        ]
        self.play(*thirdtocasdoorgroup)

        ###授权成功
        casdoortouser2 = Arrow(start=LEFT+DOWN, end=4*LEFT)
        request2 = Text("验证成功~").scale(0.6)
        request2.next_to(casdoortouser2, UP)
        self.play(Create(casdoortouser2, runtime=6))
        self.play(FadeIn(request2))

        requestout2 =[
            FadeOut(casdoortouser2),
            FadeOut(request2)
        ]
        self.play(*requestout2)

        ##访问资源
        useraccesscasdoor = Arrow(start=4*LEFT, end=LEFT+DOWN)
        useraccesscasdoortext = Text("请求访问资源！").scale(0.6)
        useraccesscasdoortext.next_to(useraccesscasdoor, UP)
        self.play(Create(useraccesscasdoor))
        self.play(FadeIn(useraccesscasdoortext))
        useraccesscasdoorgroup =[
            FadeOut(useraccesscasdoor),
            FadeOut(useraccesscasdoortext)
        ]
        self.play(*useraccesscasdoorgroup)

        ###Casdoor访问资源
        casdooraccessresource = Arrow(start=0.5*DOWN, end=1.7*UP)
        casdooraccessresourcetext = Text("访问资源~").scale(0.6)
        casdooraccessresourcetext.next_to(casdooraccessresource, LEFT)
        self.play(Create(casdooraccessresource))
        self.play(FadeIn(casdooraccessresourcetext))
        casdooraccessresourcegroup =[
            FadeOut(casdooraccessresource),
            FadeOut(casdooraccessresourcetext)
        ]
        self.play(*casdooraccessresourcegroup)


        ####清屏
        providersgroup = [
            FadeOut(resource),
            FadeOut(resources),
            FadeOut(supply),
            FadeOut(gopher),
            FadeOut(user),
            FadeOut(casdoor),
            FadeOut(weibo),
            FadeOut(gitlab),
            FadeOut(qq),
            FadeOut(linkedin),
            FadeOut(google),
            FadeOut(twitter),
            FadeOut(github),
            FadeOut(facebook),
            FadeOut(wechat),
            FadeOut(wecom),
            FadeOut(gitee),
            FadeOut(lark)
        ]
        self.play(*providersgroup)
        self.play(casbin_pic.animate.scale(0.6))
        self.play(casbin_pic.animate.to_corner(UL))
        
###############################################################################################
        ###如何使用？
        deploytext = Text("仅需几步就可部署Casdoor")
        self.play(Create(deploytext))
        self.play(FadeOut(deploytext))

        codeclone = '''
        git clone https://github.com/casbin/casdoor
        '''

        rendered_code = Code(code=codeclone, tab_width=4, background="window",
                            language="Bash", font="Monospace")

        codeclonetext = Text("克隆源码")
        codeclonetext.to_edge(UP)
        rendered_code.next_to(codeclonetext, DOWN)
        codeclonegroup =[
            FadeIn(codeclonetext),
            FadeIn(rendered_code)
        ]
        self.play(*codeclonegroup)

        frontend_code = '''
        cd web
        yarn run build
        '''
        render_frontend_code = Code(code=frontend_code, tab_width=4, background="window",
                            language="Bash", font="Monospace")
        frontendtext = Text("编译前端")
        frontendtext.move_to(2*LEFT+0.6*UP)

        
        backend_code = '''
        go build && ./casdoor
        '''
        render_backend_code = Code(code=backend_code, tab_width=4, background="window",
                            language="Bash", font="Monospace")
        backendtext = Text("编译后端并部署")
        backendtext.move_to(2.5*RIGHT+0.6*UP)

        render_backend_code.move_to(3*RIGHT+DOWN)
        render_frontend_code.move_to(3*LEFT+DOWN)


        codegroup = [
            FadeIn(backendtext),
            FadeIn(frontendtext),
            FadeIn(render_frontend_code),
            FadeIn(render_backend_code)
        ]
        self.play(*codegroup)

        codegroupclear = [
            FadeOut(rendered_code),
            FadeOut(codeclonetext),
            FadeOut(backendtext),
            FadeOut(frontendtext),
            FadeOut(render_backend_code),
            FadeOut(render_frontend_code)
        ]
        self.play(*codegroupclear)


############################################
        thanks = Text("感谢观看~")
        self.play(Create(thanks))
        self.play(FadeOut(thanks))