streamlitast로 가져오기

인쇄 (" 팩 다시 로드됨")
st.set_page_config(
    page_title="축구 도감",
    page_icon="/images/good.png"
)

성제("박비")G 축구 도감")
st.markdown("**축구선수**를 하나씩 추가해서 도감을 채워보세요!")

type_emo 지_dict = {
    "GK": "✊",
    "MF": "🐛",
    "DF": "🤖",
    "FW": "🔥"
}

initial_soccers = [
    {
    
       "name": "손흥민",
       "유형": ["FW"],
       "image_url": "https://i.namu.wiki/i/rv7nNga684J_H6QCCJeZx6l-Ii20iEa_Dj3SoO-emIBP-BDiZEpp5pO_35iX0Wfb5P569XKwJFBQtO8-I4oRs7ZfUfrpyb3mRMdS4XwLuoYpt4MkBoX0UnIa564rn-Eyei0V2TIvlPXuyzrJfEAa_6L-RhF0BJjaZ8AGXbtfVbM.webp"
    },
    {
    
       "name": "이강인",
       "유형": ["MF"],
       "image_url": "https://i.namu.wiki/i/rv7nNga684J_H6QCCJeZx7p2wimxR_XIcRWbU1O7DNdyh9NzZHn9bpfZGoR57za-GzRa5eepu09m63KAqHv1CVlStBGVSEFIQBROPVMG1khskNuvKdNscIa55iHW1OsZwLj6Cu2AkgTNiBDMDvWvkvkPuImcPgO4CuQWAs9a8gI.webp"
    },
    {
    
       "name": "황희찬",
       "유형": ["FW"],
       "image_url": "https://i.namu.wiki/i/rv7nNga684J_H6QCCJeZx6YWohj1926fjFFtoH7yhuRmI-1AeXUYCuocPFXzefakQ1gqZpoZlIMhixpzZ_-DR5MLZtBGC_YSCrxDolbBoIQPKTl9G0AOAz7cFg1v53KUymNVOSd_EDW8uzk8fMjII9QV5BHZ4NKc6Ocf5ReeOdM.webp"
    },
    {
    
       "name": "이재성",
       "유형": ["MF"],
       "image_url": "https://i.namu.wiki/i/rv7nNga684J_H6QCCJeZx1c-CL7XshFCg5UJRAc6hp2YhW_h-6g8M8rgwB-vdVI3gASAatq_oWnCmWwUf6XRKrgP6c2DLzPXf51vOd5lg-GsnPfc0EwOJl8KuJUjLGRaqjgMpnDdDigxhuEE9b2JKAn1INB5facyLv3EQmgsxW4.webp"
    },
    {
    
       "name": "김민재",
       "유형": ["DF"],
       "image_url": "https://i.namu.wiki/i/rv7nNga684J_H6QCCJeZx7Yb1g0uDa9QxCdDLgPiP2AQ2jn8lr-24-bN-2I2Lvm5DinyXVxzezlPdjI8JT_C8KAoN4cI44Zu32TXAaO7wDzkgNJhRUjGxKgsZD-jqn4VCgXgmRb_nkxUWLk-P43Ng4ILW8AhRKXxn9erPIrxqm8.webp"
    },
    {
    
       "name": "조현우",
       "유형": ["GK"],
       "image_url": "https://i.namu.wiki/i/rv7nNga684J_H6QCCJeZx4QlJ3bFSk2Cn9Dk279juuGqW691dlWJE-Gsh5c-Ufh20z-_WkZq9cgZUX0vk3CPJ4dpbjgRScRDbHNn897d_Ip1ChnhhUzICoI5mJ4T2g0oENMsDQj8FgEWUHPH9GLe7S20bP9HnEXCKFIl2uc2L0U.webp"
    },
]

예제_soccer = {
    "name": "김영권",
 "유형": ["DF"],
 "image_url": "https://i.namu.wiki/i/rv7nNga684J_H6QCCJeZx2lQ_D-HXDZ6z2AxjYDqg5Bur_Ef9uTg3KkpngBrP1G2lO6uD3p5OR-5hCZscETPrRScMxKFTH9Lov9kjCbUnzfZrINZDX1Hdx69xY0vvuQ14VzA97H3Bgq7QjRJQpZofAGuJLgDGcsuSV5PVk1lZtE.webp"
}



"축구"가 st. session_state에 없는 경우:
    st.session_state.축구선수들 = 이니셜_축구선수들


auto_complete = st.toggle("예시 데이터로 채우기")
인쇄 (" peqe_reload, auto_complete, auto_complete)
st.form(key="form")과 함께:
    col1, col2 = st. columns(2)
    col1:
       name = st.text_input(
        label="축구선수 이름",
        value = example_soccer["이름"]을(를) auto_complete인 경우 ""
       )
    col2:
       type = st.multisselect(
       label="축구선수 포지션", 
       options= list(type_emoji_dict.keys ()),
       max_selections=2,
       auto_complete other [ ]인 경우 default = example_soccer["type"]
)
    image_url =st.text_input(
        label="축구선수 이미지 URL",
        value=example_soccer["image_url"](자동_완전한 경우) 그렇지 않으면 ""
        )
    submit = st.form_submit_button (label="Submit")
    제출하는 경우:
        이름이 아닌 경우:
            st.error("축구선수의 이름을 입력해주세요.")
        엘리플렌(유형) == 0:
            st.error("축구선수의 포지션을 적어도 한개 선택해주세요.")
        기타:
            st.success("축구선수를 추가할 수 있습니다.")
            st.session_state.축구, append({
                "이름": 이름,
                "유형": 유형,
                "image_url" : image_url가 아닌 경우 image_url "/images/default.png"
            })
            



i in range(0, len(st. session_state)의 경우.축구), 3):
     low_soccers = st. session_state.soccers[i:i+3]
     cols = st. columns(3)
     j 범위의 경우(len(row_soccers)):
         cols[j]:
             축구=열_축구[j]
             st. expander(label=f"**{i+j+1} 포함). {soccer['name']}**", expanded=True):
                st.image(soccer["image_url"])
                emoji_types = [f"{type_emoji_dict[x]} {x}" for x soccer["types"]]
                st.서브헤더 (" / .join(emo ji_types)
                delete_button = st.button (label="삭제", key=i+j, use_container_width=True)
                delete_button인 경우:
                    인쇄 (" 삭제 버튼 클릭!)
                    del st.session_state.축구 선수[i+j]
                    성 rerun()







