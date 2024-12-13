select  
  r.data_mensal,
  r.semana_mes,
  (SELECT sb.descricao_valor
    FROM `quantum-device-443518-b1.pnad_covid.dominio` sa inner join 
        `quantum-device-443518-b1.pnad_covid.valores` sb on
        sa.codigo = sb.cod_tabela
    where sa.codigo = 'UF' and CAST(sb.valor AS INT64)  = r.UF
  ) UF,
  (SELECT sb.descricao_valor
    FROM `quantum-device-443518-b1.pnad_covid.dominio` sa inner join 
        `quantum-device-443518-b1.pnad_covid.valores` sb on
        sa.codigo = sb.cod_tabela
    where sa.codigo = 'RM_RIDE' and upper(sb.valor) = upper(r.RM_RIDE)
  ) regiao_metropolitana,
  r.situacao_domicilio,
  r.codigo,
  r.descricao,  
  r.descricao_valor,
  r.qt
from (
  SELECT 
    a.codigo, 
    a.descricao, 
    COALESCE(b.descricao_valor, 'Não aplicável') AS descricao_valor,
    -- Campo de data baseado no valor de V1013
    CASE 
      WHEN v.V1013 = 7 THEN DATE('2024-07-01')
      WHEN v.V1013 = 8 THEN DATE('2024-08-01')
      WHEN v.V1013 = 9 THEN DATE('2024-09-01')
      ELSE NULL
    END AS data_mensal,
    v.RM_RIDE,
    v.UF,
    v.V1012 as semana_mes,
    CASE 
      WHEN v.V1022 = 1 THEN 'Urbana'
      WHEN v.V1022 = 2 THEN 'Rural'
      ELSE NULL
    END AS situacao_domicilio,
    -- Total 
    COUNT(1) AS qt
  FROM 
    `quantum-device-443518-b1.pnad_covid.pnad_covid` v
  JOIN 
    `quantum-device-443518-b1.pnad_covid.dominio` a 
    ON a.codigo = 'B009B'
  LEFT JOIN 
    `quantum-device-443518-b1.pnad_covid.valores` b 
    ON b.cod_tabela = a.codigo 
    AND CAST(b.valor AS INT64)  = v.B009B
  GROUP BY 
    a.codigo, a.descricao, b.descricao_valor, v.V1013, v.RM_RIDE, v.UF, V1012, v.V1022
) r