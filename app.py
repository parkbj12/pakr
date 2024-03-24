import streamlit as st

print("paqe reloaded")
st.set_page_config(
    page_title="축구 도감",
    page_icon="./images/good.png"
)

st.title("Park B.G 축구 도감")
st.markdown("**축구선수**를 하나씩 추가해서 도감을 채워보세요!")

type_emoji_dict = {
    "GK": "✊",
    "MF": "🐛",
    "DF": "🤖",
    "FW": "🔥"
}

initial_soccers = [
    {
    
       "name": "손흥민",
       "types": ["FW"],
       "image_url": "https://i.namu.wiki/i/rv7nNga684J_H6QCCJeZx6l-Ii20iEa_Dj3SoO-emIBP-BDiZEpp5pO_35iX0Wfb5P569XKwJFBQtO8-I4oRs7ZfUfrpyb3mRMdS4XwLuoYpt4MkBoX0UnIa564rn-Eyei0V2TIvlPXuyzrJfEAa_6L-RhF0BJjaZ8AGXbtfVbM.webp"
    },
    {
    
       "name": "이강인",
       "types": ["MF"],
       "image_url": "https://i.namu.wiki/i/rv7nNga684J_H6QCCJeZx7p2wimxR_XIcRWbU1O7DNdyh9NzZHn9bpfZGoR57za-GzRa5eepu09m63KAqHv1CVlStBGVSEFIQBROPVMG1khskNuvKdNscIa55iHW1OsZwLj6Cu2AkgTNiBDMDvWvkvkPuImcPgO4CuQWAs9a8gI.webp"
    },
    {
    
       "name": "황희찬",
       "types": ["FW"],
       "image_url": "https://i.namu.wiki/i/rv7nNga684J_H6QCCJeZx6YWohj1926fjFFtoH7yhuRmI-1AeXUYCuocPFXzefakQ1gqZpoZlIMhixpzZ_-DR5MLZtBGC_YSCrxDolbBoIQPKTl9G0AOAz7cFg1v53KUymNVOSd_EDW8uzk8fMjII9QV5BHZ4NKc6Ocf5ReeOdM.webp"
    },
    {
    
       "name": "이재성",
       "types": ["MF"],
       "image_url": "https://i.namu.wiki/i/rv7nNga684J_H6QCCJeZx1c-CL7XshFCg5UJRAc6hp2YhW_h-6g8M8rgwB-vdVI3gASAatq_oWnCmWwUf6XRKrgP6c2DLzPXf51vOd5lg-GsnPfc0EwOJl8KuJUjLGRaqjgMpnDdDigxhuEE9b2JKAn1INB5facyLv3EQmgsxW4.webp"
    },
    {
    
       "name": "김민재",
       "types": ["DF"],
       "image_url": "https://i.namu.wiki/i/rv7nNga684J_H6QCCJeZx7Yb1g0uDa9QxCdDLgPiP2AQ2jn8lr-24-bN-2I2Lvm5DinyXVxzezlPdjI8JT_C8KAoN4cI44Zu32TXAaO7wDzkgNJhRUjGxKgsZD-jqn4VCgXgmRb_nkxUWLk-P43Ng4ILW8AhRKXxn9erPIrxqm8.webp"
    },
    {
    
       "name": "조현우",
       "types": ["GK"],
       "image_url": "https://i.namu.wiki/i/rv7nNga684J_H6QCCJeZx4QlJ3bFSk2Cn9Dk279juuGqW691dlWJE-Gsh5c-Ufh20z-_WkZq9cgZUX0vk3CPJ4dpbjgRScRDbHNn897d_Ip1ChnhhUzICoI5mJ4T2g0oENMsDQj8FgEWUHPH9GLe7S20bP9HnEXCKFIl2uc2L0U.webp"
    },
]

example_soccer = {
    "name": "김영권",
    "types": ["DF"],
    "image_url": "https://i.namu.wiki/i/rv7nNga684J_H6QCCJeZx2lQ_D-HXDZ6z2AxjYDqg5Bur_Ef9uTg3KkpngBrP1G2lO6uD3p5OR-5hCZscETPrRScMxKFTH9Lov9kjCbUnzfZrINZDX1Hdx69xY0vvuQ14VzA97H3Bgq7QjRJQpZofAGuJLgDGcsuSV5PVk1lZtE.webp"
}



if"soccers" not in st.session_state:
    st.session_state.soccers = initial_soccers


auto_complete = st.toggle("예시 데이터로 채우기")
print("peqe_reload, auto_complete", auto_complete)
with st.form(key="form"):
    col1, col2 = st.columns(2)
    with col1:
       name = st.text_input(
        label="축구선수 이름",
        value=example_soccer["name"] if auto_complete else ""
       )
    with col2:
       types = st.multiselect(
       label="축구선수 포지션", 
       options=list(type_emoji_dict.keys()),
       max_selections=2,
       default=example_soccer["types"] if auto_complete else []
)
    image_url = st.text_input(
        label="축구선수 이미지 URL",
        value=example_soccer["image_url"] if auto_complete else ""
        )
    submit = st.form_submit_button(label="Submit")
    if submit:
        if not name:
            st.error("축구선수의 이름을 입력해주세요.")
        elif len(types) == 0:
            st.error("축구선수의 포지션을 적어도 한개 선택해주세요.")
        else:
            st.success("축구선수를 추가할 수 있습니다.")
            st.session_state.soccers.append({
                "name": name,
                "types": types,
                "image_url" : image_url if image_url else "./images/default.png"
            })
            



for i in range(0, len(st.session_state.soccers), 3):
     row_soccers = st.session_state.soccers[i:i+3]
     cols = st.columns(3)
     for j in range(len(row_soccers)):
         with cols[j]:
             soccer = row_soccers[j]
             with st.expander(label=f"**{i+j+1}. {soccer['name']}**", expanded=True):
                st.image(soccer["image_url"])
                emoji_types = [f"{type_emoji_dict[x]} {x}" for x in soccer["types"]]
                st.subheader(" / ".join(emoji_types))
                delete_button = st.button(label="삭제", key=i+j, use_container_width=True)
                if delete_button:
                    print("delete button clicked!")
                    del st.session_state.soccers[i+j]
                    st.rerun()







