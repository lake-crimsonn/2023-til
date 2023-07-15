using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HandTracking : MonoBehaviour
{
    // UDP 
    public UDPReceive udpReceive;
    // 랜드마크 오브젝트 담는 리스트
    public GameObject[] handPoints; 

    void Start()
    {
        
    }

    void Update()
    {
        // UDP에서 받아온 data
        string data = udpReceive.data; 

        if ( data.Length != 0 ) 
        {

            // data의 양쪽 대괄호 지우기
            data = data.Trim(new char[]{'[',']'});
            //print(data);

            // 쉼표를 기준으로 데이터 하나씩 가져오기
            string[] points = data.Split(',');
            print(points[0]);

            // 플로트화하기
            for(int i = 0; i < 21; i++)
            {
                // x,y,z값 가져와서 플로트화하고 스케일링
                // 캠화면과 유니티 화면이 1:1로 매칭되지 않기 때문에 알맞은 수치를 찾아야 함
                float x = float.Parse(points[i*3])/80-8; 
                float y = float.Parse(points[i*3+1])/80-5; 
                float z = float.Parse(points[i*3+2])/80; 

                handPoints[i].transform.localPosition = new Vector3(x,y,z);
            }

        }

    }
}
